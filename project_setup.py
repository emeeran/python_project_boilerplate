import os
import subprocess


def run_subprocess(commands, project_path):
    for command in commands:
        subprocess.run(
            command,
            cwd=project_path,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )


def create_project():
    parent_dir = input("Enter the parent directory path: ")
    project_name = input("Enter the project directory name: ")
    subdirectories = ["docs", "src", "data", "notes", "tests", "img", ".vscode"]
    files_to_create = ["README.md", "scribble.md", ".env"]
    special_files = {"src": ["main.py", "__init__.py"]}

    project_path = os.path.join(parent_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    for subdir in subdirectories:
        subdir_path = os.path.join(project_path, subdir)
        os.makedirs(subdir_path, exist_ok=True)
        for file_name in special_files.get(subdir, []):
            open(os.path.join(subdir_path, file_name), "w").close()

    for file_name in files_to_create:
        open(os.path.join(project_path, file_name), "w").close()

    commands = [
        "python -m venv .venv",
        ".venv\\scripts\\activate"
        ".venv\\Scripts\\python -m pip install --upgrade pip",
        ".venv\\Scripts\\python -m pip install flake8",
        ".venv\\Scripts\\python -m pip install pre-commit",
        ".venv\\Scripts\\pre-commit install",
        "git init",
        "git add .",
        "git commit -m 'Initial commit'",
    ]
    run_subprocess(commands, project_path)

    # Example of breaking a dictionary assignment into multiple lines
    file_contents = {
        ".flake8": "[flake8]\nmax-line-length = 120\nexclude = .git,__pycache__\n",
        ".pre-commit-config.yaml": (
            "repos:\n"
            " - repo: https://github.com/PyCQA/flake8\n"
            "    rev: 4.0.1\n"
            "    hooks:\n"
            "      - id: flake8\n"
            "        args: [--max-line-length=120]\n"
        ),
        ".gitignore": open("git_contents.txt", "r").read(),
        "README.md": open("readme_content.txt", "r").read(),
    }

    for file_name, content in file_contents.items():
        with open(os.path.join(project_path, file_name), "w") as f:
            f.write(content)


if __name__ == "__main__":
    create_project()
