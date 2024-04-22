import os
import subprocess

def create_project():
    project_path = input("Enter the path where you want to create the project directory: ")
    project_name = input("Enter the project name: ")
    project_dir = os.path.join(project_path, project_name)
    os.makedirs(project_dir, exist_ok=True)

    structure = {
        '': ['.gitignore', '.env', 'README.md'],
        'src': ['__init__.py', 'main.py'],
        'docs': [],
        'notes': [],
        '.vscode': ['settings.json'],
        'data': [],
        'tests': [],
        'img': []
    }

    for dir_path, files in structure.items():
        full_path = os.path.join(project_dir, dir_path)
        os.makedirs(full_path, exist_ok=True)
        for file_name in files:
            open(os.path.join(full_path, file_name), 'w').close()

    file_contents = {
        '.gitignore': 'git_contents.txt',
        'README.md': 'readme_content.txt',
        '.vscode/settings.json': 'json_content.txt'
    }

    for file_path, content_file in file_contents.items():
        with open(content_file, 'r') as src, open(os.path.join(project_dir, file_path), 'w') as dst:
            dst.write(src.read())

    venv_path = os.path.join(project_dir, '.venv')
    subprocess.run(["python", "-m", "venv", venv_path], check=True)

    subprocess.run(["git", "-C", project_dir, "init"])
    subprocess.run(["git", "-C", project_dir, "add", "."])
    subprocess.run(["git", "-C", project_dir, "commit", "-m", "Initial Commit"])

    print("Project setup complete. Please activate the virtual environment manually.")

if __name__ == "__main__":
    create_project()
