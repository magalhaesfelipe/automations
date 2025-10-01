#!/usr/bin/env python3
import os
import subprocess
import sys

npm_cmd = "npm.cmd" if sys.platform == "win32" else "npm"

# ROOT DIRECTORY (../fe)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

dirs = [
    "home-app",
    "triagem-app",
    "login-app",
    "orcamento-app",
    "root-app",
    "config-app",
    "cadastro-app",
    "agenda-app",
]

# UPDATE
for d in dirs:
    full_path = os.path.join(BASE_DIR, d)

    if not os.path.isdir(full_path):
        print(f"Directory {full_path} does not exist. Skipping...")
        continue

    if not os.path.isdir(os.path.join(full_path, ".git")):
        print(f"Skipping {full_path} (not a git repo)")
        continue

    print(f"\n -> UPDATING {d}...\n")
    try:
        subprocess.run(["git", "-C", full_path, "pull"], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to update {d}")

print("\n -> FINISHED UPDATES \n")

# INSTALL PACKAGES
print("\n -> INSTALLING PACKAGES \n")

for d in dirs:
    full_path = os.path.join(BASE_DIR, d)

    if not os.path.isdir(full_path):
        print(f"Directory {full_path} does not exist. Skipping...")
        continue

    if not os.path.isfile(os.path.join(full_path, "package.json")):
        print(f"Skipping {d} (no package.json found)")
        continue

    print(f"\nInstalling packages in {d}...\n")
    try:
        subprocess.run([npm_cmd, "install"], cwd=full_path, check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install packages in {d}")

# LAUNCH
print("\n -> LAUNCHING...\n")
try:
    subprocess.run([npm_cmd, "start"], cwd=BASE_DIR, check=True)
except subprocess.CalledProcessError:
    print("Failed to launch main app")
