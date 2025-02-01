import subprocess
import tempfile
import os
from google.cloud import aiplatform

def init_aiplatform():
    service_account = "path/to/your/service_account.json"
    aiplatform.init(project="your-project-id", location="us-central1", credentials=service_account)

def convert_python_code(py3_code):
    prompt = (
        "Convert the following Python 3 code to be fully compatible with Python 2. "
        "Ensure that all incompatible features, such as f-strings, type hints, "
        "dataclasses, and print function syntax, are correctly refactored. "
        "The output should be a complete and executable Python script without additional explanations. "
        "Strictly maintain the original logic and functionality.\n\n"
        f"{py3_code}"
    )
    model = "gemini-pro"
    response = aiplatform.Predictor(endpoint_id="your-endpoint-id").predict(instances=[{"content": prompt}])
    return response.predictions[0]["content"]

def run_python_code(py2_code):
    with tempfile.TemporaryDirectory() as temp_dir:
        py_file = os.path.join(temp_dir, "script.py")
        
        with open(py_file, "w") as f:
            f.write(py2_code)
        
        run_result = subprocess.run(["python2", py_file], capture_output=True, text=True)
        return run_result.stdout if run_result.returncode == 0 else f"Execution failed:\n{run_result.stderr}"

if __name__ == "__main__":
    init_aiplatform()
    input_file_path = "path/to/python3_code.py"  # 指定 Python 3 代碼的文件路徑
    
    with open(input_file_path, "r") as file:
        python3_code = file.read()
    
    python2_code = convert_python_code(python3_code)
    print("Converted Code:\n", python2_code)
    
    result = run_python_code(python2_code)
    print("Execution Result:\n", result)
