#!/usr/bin/env python3
import os
import subprocess

dirs = [
    "app-home",
    "app-triagem",
    "app-login",
    "app-orcamento",
    "app-root",
    "app-config",
    "app-cadastro",
    "app-agenda",
]


for d in dirs:
    if not os.path.isdir(d):
        print(f"Directory {d} does not exist. Skipping...")
        continue

    if not os.path.isdir(os.path.join(d, ".git")):
        print(f"Skipping {d} (not a git repo)")
        continue

    print()
    print(f"Updating {d}...")
    print()
    try:
        subprocess.run(["git", "-C", d, "pull"], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to update {d}")

print()
print(f"##### Finished updates #####")
print()

print()
print(f"#### Installing packages ####")
print()

for d in dirs:
    if not os.path.isdir(d):
        print(f"Directory {d} does not exist. Skipping...")
        continue

    if not os.path.isfile(os.path.join(d, "package.json")):
        print(f"Skipping {d} (no package.json config found)")
        continue

    print()
    print(f"Installing packages in {d}...")
    print()
    try:
        subprocess.run(["npm", "install"], cwd=d, check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install packages in {d}")

print(f"Launching")
subprocess.run(["npm", "start"], check=True)
print()
