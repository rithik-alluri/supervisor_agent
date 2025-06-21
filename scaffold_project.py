import os

# Use current working directory as the project root
project_root = os.getcwd()

structure = {
    "nodes": [
        "__init__.py",
        "supervisor.py",
        "comparison_stub.py",
        "deepdive_stub.py",
        "fallback_stub.py"
    ],
    "config": [
        "settings.yaml"
    ],
    "tests": [
        "__init__.py",
        "test_graph.py"
    ],
    "tests/test_nodes": [
        "__init__.py",
        "test_comparison.py"
    ],
    "": [
        "agent_graph.py",
        "llm_config.py",
        "main.py",
        "README.md",
        ".gitignore",
        "requirements.txt",
        ".env"
    ]
}

for folder, files in structure.items():
    folder_path = os.path.join(project_root, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                if file_name == "__init__.py":
                    f.write("# Marks this folder as a Python package\n")
                elif file_name == ".gitignore":
                    f.write(".venv/\n__pycache__/\n.env\n*.pyc\n")
                elif file_name == "README.md":
                    f.write("# Supervisor Agent Project\n")
                elif file_name == "requirements.txt":
                    f.write("# Project dependencies\n")
                elif file_name == ".env":
                    f.write("# Environment variables (e.g., API keys)\n")
                else:
                    f.write(f"# {file_name} placeholder\n")

print("Scaffolding completed")