import os, shutil

# Your custom path
downloads = r"C:\Users\rgm-79N\Documents\2501\daunrodo"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Docs": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Zips": [".zip", ".rar", ".7z"],
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Scripts": [".py", ".js", ".bat", ".sh"]
}

# Organize files
for file in os.listdir(downloads):
    src = os.path.join(downloads, file)
    if os.path.isfile(src):
        ext = os.path.splitext(file)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                dst_folder = os.path.join(downloads, folder)
                os.makedirs(dst_folder, exist_ok=True)
                shutil.move(src, dst_folder)
                print(f"Moved: {file} → {folder}")
                break
