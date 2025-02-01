import subprocess
import tempfile
import os
from google.cloud import aiplatform

def init_aiplatform():
    service_account = "path/to/your/service_account.json"
    aiplatform.init(project="your-project-id", location="us-central1", credentials=service_account)

def convert_java_to_python(java_code):
    prompt = (
        "Convert the following Java code to Python while preserving its logic and functionality. "
        "Ensure that all Java-specific constructs, such as static typing, class-based structures, and threading, "
        "are properly adapted to Python idioms. The output should be a complete and executable Python script "
        "without additional explanations. Strictly maintain the original logic and behavior.\n\n"
        f"{java_code}"
    )
    model = "gemini-pro"
    response = aiplatform.Predictor(endpoint_id="your-endpoint-id").predict(instances=[{"content": prompt}])
    return response.predictions[0]["content"]

def run_python_code(py_code):
    with tempfile.TemporaryDirectory() as temp_dir:
        py_file = os.path.join(temp_dir, "script.py")
        
        with open(py_file, "w") as f:
            f.write(py_code)
        
        run_result = subprocess.run(["python3", py_file], capture_output=True, text=True)
        return run_result.stdout if run_result.returncode == 0 else f"Execution failed:\n{run_result.stderr}"

if __name__ == "__main__":
    init_aiplatform()
    input_file_path = "path/to/java_code.java"  # 指定 Java 代碼的文件路徑
    
    with open(input_file_path, "r") as file:
        java_code = file.read()
    
    python_code = convert_java_to_python(java_code)
    print("Converted Code:\n", python_code)
    
    result = run_python_code(python_code)
    print("Execution Result:\n", result)
