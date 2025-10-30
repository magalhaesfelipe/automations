import subprocess
import os

url = "http://example.com"

# Paths
browser = r"C:\Program Files\BraveSoftware\Brave-Browser-Beta\Application\brave.exe"
editor = r"C:\Program Files\Microsoft VS Code\Code.exe"
directory = r"C:\example"

# Browser
if os.path.exists(browser):
    subprocess.Popen([browser, url])

# Editor
if os.path.exists(editor):
    subprocess.Popen([editor, directory])
