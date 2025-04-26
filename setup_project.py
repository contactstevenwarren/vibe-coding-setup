#!/usr/bin/env python3

from pathlib import Path
import sys

def get_project_name():
    """Prompt the user for a project name and validate it."""
    while True:
        project_name = input("Enter project name: ").strip()
        if project_name:
            return project_name
        print("Error: Project name cannot be empty. Please try again.")

def get_project_description():
    """Prompt the user for a project description."""
    return input("Enter a brief project description: ").strip()

def create_project_directory(project_name):
    """Create the root project directory. Exit if it already exists."""
    project_path = Path.cwd() / project_name
    
    if project_path.exists():
        print(f"Error: Directory '{project_name}' already exists. Please choose a different name.")
        sys.exit(1)
    
    try:
        project_path.mkdir()
        print(f"Created project directory: {project_path}")
        return project_path
    except Exception as e:
        print(f"Error creating project directory: {e}")
        sys.exit(1)

def create_subdirectories(project_path):
    """Create required subdirectories within the project directory."""
    memory_bank_path = project_path / "memory-bank"
    cursor_path = project_path / ".cursor"
    
    try:
        memory_bank_path.mkdir(parents=True, exist_ok=True)
        cursor_path.mkdir(parents=True, exist_ok=True)
        print(f"Created subdirectory: {memory_bank_path}")
        print(f"Created subdirectory: {cursor_path}")
        return memory_bank_path, cursor_path
    except Exception as e:
        print(f"Error creating subdirectories: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Vibe Coding Project Setup Script")
    project_name = get_project_name()
    project_description = get_project_description()
    project_path = create_project_directory(project_name)
    memory_bank_path, cursor_path = create_subdirectories(project_path)
    
    print(f"Project name: {project_name}")
    print(f"Project description: {project_description}")
    print(f"Project directory: {project_path}")
    # Later steps will add more functionality here 