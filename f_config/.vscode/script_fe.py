#!/usr/bin/env python3
import os
import subprocess

dirs = ["home", "triagem", "login", "orcamento", "root", "config", "cadastro", "agenda"]


for d in dirs:
    if not os.path.isdir(d):
        print(f"Directory {d} does not exist. Skipping...")
        continue

    if not os.path.isdir(os.path.join(d, ".git")):
        print(f"Skipping {d} (not a git repo)")
        continue

    print(f"Updating {d}...")
    try:
        subprocess.run(["git", "-C", d, "pull"], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to update {d}")

print()
print(f"##### Finished updates #####")
print()

print(f"Launching")
subprocess.run(["npm", "start"], shell=True, check=True)
print()
