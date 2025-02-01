import subprocess
import tempfile
import os
from google.cloud import aiplatform

def init_aiplatform():
    service_account = "path/to/your/service_account.json"
    aiplatform.init(project="your-project-id", location="us-central1", credentials=service_account)

def convert_java_code(java_code):
    prompt = (
        "Convert the following Java 21 code to be fully compatible with JDK 8. "
        "Ensure that all features unsupported in JDK 8, such as var, records, "
        "sealed classes, and switch expressions, are correctly refactored. "
        "The output should be a complete and executable Java class without additional explanations. "
        "Strictly maintain the original logic and functionality.\n\n"
        f"{java_code}"
    )
    model = "gemini-pro"
    response = aiplatform.Predictor(endpoint_id="your-endpoint-id").predict(instances=[{"content": prompt}])
    return response.predictions[0]["content"]

def compile_and_run(java_code):
    with tempfile.TemporaryDirectory() as temp_dir:
        java_file = os.path.join(temp_dir, "Main.java")
        
        with open(java_file, "w") as f:
            f.write(java_code)
        
        compile_result = subprocess.run(["javac", java_file], capture_output=True, text=True)
        if compile_result.returncode != 0:
            return f"Compilation failed:\n{compile_result.stderr}"
        
        run_result = subprocess.run(["java", "-cp", temp_dir, "Main"], capture_output=True, text=True)
        return run_result.stdout if run_result.returncode == 0 else f"Execution failed:\n{run_result.stderr}"

if __name__ == "__main__":
    init_aiplatform()
    input_file_path = "path/to/java21_code.java"  # 指定 Java 21 代碼的文件路徑
    
    with open(input_file_path, "r") as file:
        java21_code = file.read()
    
    jdk8_code = convert_java_code(java21_code)
    print("Converted Code:\n", jdk8_code)
    
    result = compile_and_run(jdk8_code)
    print("Execution Result:\n", result)
