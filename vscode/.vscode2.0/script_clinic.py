#!/usr/bin/env python3
import os
import subprocess
import sys

npm_cmd = "npm.cmd" if sys.platform == "win32" else "npm"

# DIRECTORIES PATH (root, front, back)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
front_path = os.path.join(BASE_DIR, "front")
# back_path = os.path.join(BASE_DIR, "back")

front_dirs = [
    "front/root",
    "front/home",
    "front/configuracoes",
    "front/cadastro",
    "front/agenda",
    "front/orcamento",
    "front/triagem",
    # "front/login",
]

# UPDATE BACK
# print("\n 🔶 -> UPDATING BACK \n")
# try:
#     subprocess.run(["git", "-C", back_path, "pull"], check=True)
# except subprocess.CalledProcessError:
#     print(f"⚠️ Failed to update backend in: {back_path}")


# UPDATE FRONT
print("\n 🔷 -> UPDATING FRONT \n")
for d in front_dirs:
    full_path = os.path.join(BASE_DIR, d)

    if not os.path.isdir(full_path):
        print(f"🪹 Directory {full_path} does not exist. Skipping...")
        continue

    if not os.path.isdir(os.path.join(full_path, ".git")):
        print(f"Skipping {full_path} (not a git repo)")
        continue

    print(f"\n 🐫 -> UPDATING {d}...\n")
    try:
        subprocess.run(["git", "-C", full_path, "pull"], check=True)
    except subprocess.CalledProcessError:
        print(f"⚠️ Failed to update frontend in: {d}")

print("\n 🦅 -> FINISHED UPDATES \n")

# INSTALL PACKAGES
# print("\n -> INSTALLING PACKAGES \n")

# for d in front_dirs:
#     full_path = os.path.join(BASE_DIR, d)

#     if not os.path.isdir(full_path):
#         print(f"Directory {full_path} does not exist. Skipping...")
#         continue

#     if not os.path.isfile(os.path.join(full_path, "package.json")):
#         print(f"Skipping {d} (no package.json found)")
#         continue

#     print(f"\nInstalling packages in {d}...\n")
#     try:
#         subprocess.run([npm_cmd, "install"], cwd=full_path, check=True)
#     except subprocess.CalledProcessError:
#         print(f"Failed to install packages in {d}")

# LAUNCH
print("\n 🐢 -> LAUNCHING FRONTEND...\n")
try:
    subprocess.run([npm_cmd, "start"], cwd=front_path, check=True)
except subprocess.CalledProcessError:
    print("Failed to launch main app!")
