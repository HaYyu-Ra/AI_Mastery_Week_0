import os

# Define the base path
base_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312"

# Define the folder structure
folders = [
    ".vscode",
    ".github/workflows",
    "src",
    "notebooks",
    "tests",
    "scripts"
]

files = {
    ".vscode/settings.json": "",
    ".github/workflows/unittests.yml": "",
    ".gitignore": "",
    "requirements.txt": "",
    "README.md": "",
    "notebooks/__init__.py": "",
    "notebooks/README.md": "",
    "tests/__init__.py": "",
    "scripts/__init__.py": "",
    "scripts/README.md": ""
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files
for file, content in files.items():
    with open(os.path.join(base_path, file), 'w') as f:
        f.write(content)

print("Folder structure created successfully!")
