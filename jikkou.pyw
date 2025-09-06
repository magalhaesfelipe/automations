import subprocess
import os

# Paths
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser-Beta\Application\brave.exe"
vscode_path = r"C:\Users\rgm-79N\AppData\Local\Programs\Microsoft VS Code\Code.exe"

url = "http://localhost:9000/agenda"

# Directories
fe_dir = r"C:\2501\workspace\clinic\fe"
be_dir = r"C:\2501\workspace\clinic\be"

# --- Open Brave ---
# Check if Brave exists
if not os.path.exists(brave_path):
    print("Brave browser not found. Please check the installation path.")
else:
    # Open Brave with the specified website
    subprocess.Popen([brave_path, url])
    print(f"Brave browser launched and opened {url}!")

# --- Open VS Code windows ---
if os.path.exists(vscode_path):
    subprocess.Popen([vscode_path, fe_dir])
    print(f"VS Code opened in {fe_dir}")

    subprocess.Popen([vscode_path, be_dir])
    print(f"VS Code opened in {be_dir}")
else:
    print("VS Code not found. Please check the installation path.")
