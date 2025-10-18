import subprocess
import os

# Paths
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser-Beta\Application\brave.exe"
vscode_path = r"C:\Program Files\Microsoft VS Code\Code.exe"

url = "http://localhost:9000/cadastro"

# Directories
clinic_dir = r"C:\Users\rgm-79N\Documents\2501\sagyoba\clinic"

# --- Open Brave ---
# Check if Brave exists
if not os.path.exists(brave_path):
    print("Brave browser not found. Please check the installation path.")
else:
    # Open Brave with the specified website
    subprocess.Popen([brave_path, url])
    print(f"Brave browser launched and opened {url}!")

# --- Open VS Code window ---
if os.path.exists(vscode_path):
    subprocess.Popen([vscode_path, clinic_dir])
    print(f"VS Code opened in {clinic_dir}")

else:
    print("VS Code not found. Please check the installation path.")
