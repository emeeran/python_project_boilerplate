import os
import shutil

def create_project():
    # Prompt user for project dir path
    project_path = input("Enter the path where you want to create the project directory: ")
    # Prompt user for project name
    project_name = input("Enter the project name: ")

    # Create project directory
    project_dir = os.path.join(project_path, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Sub-directories and files to create
    sub_dirs = ['src', 'docs', 'notes', '.vscode', 'data', 'tests', 'img']
    root_files = ['.gitignore', '.env', 'README.md']
    src_files = ['__init__.py', 'main.py']
    vscode_files = ['settings.json']

    # Create sub-directories
    for sub_dir in sub_dirs:
        os.makedirs(os.path.join(project_dir, sub_dir), exist_ok=True)

    # Create root directory files
    for file_name in root_files:
        with open(os.path.join(project_dir, file_name), 'w') as f:
            pass

    # Create src directory files
    src_dir = os.path.join(project_dir, 'src')
    for file_name in src_files:
        with open(os.path.join(src_dir, file_name), 'w') as f:
            pass

    # Create .vscode directory files
    vscode_dir = os.path.join(project_dir, '.vscode')
    for file_name in vscode_files:
        with open(os.path.join(vscode_dir, file_name), 'w') as f:
            pass

    # Read content from files and write to corresponding files
    with open('git_contents.txt', 'r') as f:
        git_contents = f.read()
    with open(os.path.join(project_dir, '.gitignore'), 'w') as f:
        f.write(git_contents)

    with open('readme_content.txt', 'r') as f:
        readme_content = f.read()
    with open(os.path.join(project_dir, 'README.md'), 'w') as f:
        f.write(readme_content)

    with open('json_content.txt', 'r') as f:
        json_content = f.read()
    with open(os.path.join(vscode_dir, 'settings.json'), 'w') as f:
        f.write(json_content)

    # Create .venv and activate
    os.system(f"python -m venv {os.path.join(project_dir, '.venv')}")
    activate_path = os.path.join(project_dir, '.venv', 'Scripts', 'activate')
    os.system(f"call {activate_path}")

    # Initialize git repository
    os.chdir(project_dir)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial Commit"')

    # Open cmd window
    os.system("start cmd")

if __name__ == "__main__":
    create_project()
