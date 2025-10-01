#!/usr/bin/env python3
import os
import subprocess

# Define the project root (one directory up from .vscode)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

print(f"Updating clinic api in {project_root}...")

if not os.path.isdir(os.path.join(project_root, ".git")):
    print(f"Directory {project_root} is not a git repository. Skipping...")
else:
    try:
        subprocess.run(["git", "-C", project_root, "pull"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to update repository.")

print()
print("##### FINISHED UPDATES #####")
print()

print("LAUNCHING...")
try:
    subprocess.run(["npm", "start"], shell=True, check=True)
except subprocess.CalledProcessError:
    print("Failed to launch")
