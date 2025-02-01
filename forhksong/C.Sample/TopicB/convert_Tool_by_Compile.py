import subprocess
import tempfile
import os
import re
from google.cloud import aiplatform

def init_aiplatform():
    service_account = "path/to/your/service_account.json"
    aiplatform.init(project="your-project-id", location="us-central1", credentials=service_account)

def detect_language(code):
    if re.search(r"class\s+\w+|public\s+static\s+void\s+main", code):
        return "java"
    elif re.search(r"def\s+\w+|import\s+|print\s*\(", code):
        return "python"
    return "unknown"

def run_code(code, language):
    with tempfile.TemporaryDirectory() as temp_dir:
        file_name = "script.java" if language == "java" else "script.py"
        file_path = os.path.join(temp_dir, file_name)
        
        with open(file_path, "w") as f:
            f.write(code)
        
        if language == "java":
            compile_result = subprocess.run(["javac", file_path], capture_output=True, text=True)
            if compile_result.returncode != 0:
                return f"Compilation failed:\n{compile_result.stderr}"
            run_result = subprocess.run(["java", "-cp", temp_dir, "script"], capture_output=True, text=True)
        else:
            run_result = subprocess.run(["python3", file_path], capture_output=True, text=True)
        
        return run_result.stdout if run_result.returncode == 0 else f"Execution failed:\n{run_result.stderr}"

def fix_code_with_llm(code, language, error_message):
    prompt = (
        f"The following {language} code contains an error. Fix it so that it runs successfully.\n\n"
        f"Code:\n{code}\n\n"
        f"Error:\n{error_message}\n\n"
        "Provide only the corrected version of the code without additional explanations."
    )
    model = "gemini-pro"
    response = aiplatform.Predictor(endpoint_id="your-endpoint-id").predict(instances=[{"content": prompt}])
    return response.predictions[0]["content"]

if __name__ == "__main__":
    init_aiplatform()
    input_file_path = "path/to/code_file"  # 指定代碼文件路徑
    
    with open(input_file_path, "r") as file:
        code = file.read()
    
    language = detect_language(code)
    if language == "unknown":
        print("Could not determine the programming language.")
    else:
        result = run_code(code, language)
        while "failed" in result:
            print("Error detected, attempting to fix...")
            code = fix_code_with_llm(code, language, result)
            result = run_code(code, language)
        
        print("Final Corrected Code:\n", code)
        print("Execution Result:\n", result)
