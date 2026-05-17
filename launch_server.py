import os
import subprocess
import sys

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = r"C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe"

# Command to run uvicorn
cmd = [PYTHON_EXE, "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

print(f"Starting server with: {' '.join(cmd)}")
subprocess.Popen(cmd, cwd=BASE_DIR, creationflags=subprocess.CREATE_NEW_CONSOLE)
print("Server started in a new console window.")
