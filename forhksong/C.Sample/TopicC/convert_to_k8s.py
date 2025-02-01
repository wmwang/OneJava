import os
from google.cloud import aiplatform
from kubernetes import client, config
import yaml
from pathlib import Path
from typing import List, Dict, Optional

class CodeFileAnalyzer:
    """Handles code file detection and reading"""
    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)
        
    def is_code_file(self, file_path: Path) -> bool:
        """Check if the file is a potential code file"""
        code_extensions = {'.py', '.java', '.kt', '.groovy', '.scala'}
        return file_path.suffix.lower() in code_extensions
    
    def read_code_files(self) -> List[Dict[str, str]]:
        """Read all code files from the specified folder"""
        code_files = []
        
        if not self.folder_path.exists():
            raise FileNotFoundError(f"Folder not found: {self.folder_path}")
            
        for file_path in self.folder_path.rglob('*'):
            if file_path.is_file() and self.is_code_file(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_content = f.read()
                        code_files.append({
                            'path': str(file_path),
                            'content': code_content,
                            'filename': file_path.name
                        })
                except Exception as e:
                    print(f"Error reading file {file_path}: {str(e)}")
                    
        return code_files

class CodeAnalyzer:
    def __init__(self, project_id: str, location: str):
        """
        Initialize the CodeAnalyzer with Google Cloud project details
        
        Args:
            project_id (str): Google Cloud Project ID
            location (str): Google Cloud region (e.g., 'us-central1')
        """
        aiplatform.init(project=project_id, location=location)
        
    async def detect_language(self, code: str) -> dict:
        """
        Detect if the code is Python or Java using Vertex AI
        """
        prompt = f"""
        Analyze the following code and determine if it's Python or Java.
        Return your response in this JSON format:
        {{"language": "python|java", "confidence": 0.95}}
        
        Code to analyze:
        {code}
        """
        
        vertex_ai = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")
        response = vertex_ai.predict(prompt).text
        return eval(response)  # Convert string response to dict
        
    async def detect_version(self, code: str, language: str) -> str:
        """
        Detect the appropriate runtime version for the code
        """
        prompt = f"""
        Analyze the following {language} code and determine the most appropriate runtime version.
        For Python, consider features used and suggest a version like '3.8', '3.9', etc.
        For Java, suggest versions like '8', '11', '17', or '21' based on language features used.
        Return only the version number.
        
        Code to analyze:
        {code}
        """
        
        vertex_ai = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")
        return vertex_ai.predict(prompt).text.strip()
        
    async def generate_k8s_yaml(self, language: str, version: str, code: str, 
                              file_info: Optional[Dict] = None) -> str:
        """
        Generate appropriate Kubernetes YAML configuration
        """
        file_context = f"File: {file_info['filename']}" if file_info else "Code snippet"
        
        prompt = f"""
        Generate a Kubernetes YAML configuration for a {language} application.
        Context: {file_context}
        Requirements:
        - Runtime: {language} version {version}
        - Include appropriate resource limits
        - Use best practices for production deployment
        - Include necessary labels and annotations
        - Configure appropriate health checks
        - Set appropriate container name based on the filename
        
        The application code is:
        {code}
        
        Return only the YAML configuration.
        """
        
        vertex_ai = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")
        return vertex_ai.predict(prompt).text

class K8sDeployer:
    def __init__(self):
        """Initialize Kubernetes configuration"""
        config.load_kube_config()
        self.api = client.ApiClient()
        
    def deploy(self, yaml_content: str):
        """Deploy the application to Kubernetes"""
        k8s_objects = yaml.safe_load_all(yaml_content)
        for obj in k8s_objects:
            try:
                client.CustomObjectsApi(self.api).create_namespaced_custom_object(
                    group=obj["apiVersion"].split("/")[0],
                    version=obj["apiVersion"].split("/")[1],
                    namespace="default",
                    plural=obj["kind"].lower() + "s",
                    body=obj
                )
            except Exception as e:
                print(f"Error deploying {obj['kind']}: {str(e)}")

async def process_folder(folder_path: str, project_id: str, location: str):
    """Process all code files in the specified folder"""
    # Initialize analyzers
    file_analyzer = CodeFileAnalyzer(folder_path)
    code_analyzer = CodeAnalyzer(project_id=project_id, location=location)
    
    # Read all code files
    code_files = file_analyzer.read_code_files()
    
    if not code_files:
        print(f"No code files found in {folder_path}")
        return
    
    results = []
    for file_info in code_files:
        try:
            print(f"\nProcessing file: {file_info['path']}")
            
            # Detect language
            lang_info = await code_analyzer.detect_language(file_info['content'])
            print(f"Detected language: {lang_info['language']} (Confidence: {lang_info['confidence']})")
            
            # Detect version
            version = await code_analyzer.detect_version(file_info['content'], lang_info['language'])
            print(f"Recommended version: {version}")
            
            # Generate K8s YAML
            k8s_yaml = await code_analyzer.generate_k8s_yaml(
                lang_info['language'], 
                version, 
                file_info['content'],
                file_info
            )
            
            # Save results
            results.append({
                'file_path': file_info['path'],
                'language': lang_info['language'],
                'version': version,
                'k8s_yaml': k8s_yaml
            })
            
            # Save YAML to file
            yaml_path = Path(file_info['path']).with_suffix('.k8s.yaml')
            with open(yaml_path, 'w') as f:
                f.write(k8s_yaml)
            print(f"Generated Kubernetes YAML saved to: {yaml_path}")
            
        except Exception as e:
            print(f"Error processing file {file_info['path']}: {str(e)}")
    
    return results

async def main():
    # Configuration
    PROJECT_ID = "your-project-id"
    LOCATION = "us-central1"
    FOLDER_PATH = "./code-files"  # Specify your folder path here
    
    # Process all files in the folder
    results = await process_folder(FOLDER_PATH, PROJECT_ID, LOCATION)
    
    # Optional: Deploy to Kubernetes
    if results and input("Deploy to Kubernetes? (y/n): ").lower() == 'y':
        deployer = K8sDeployer()
        for result in results:
            print(f"\nDeploying {result['file_path']}...")
            deployer.deploy(result['k8s_yaml'])

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

