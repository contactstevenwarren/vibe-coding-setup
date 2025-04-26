# System Architecture Overview

**Project:** Vibe Coding Project Setup Script

## File/Component Index

* `setup_project.py`: Main script file that implements the Vibe Coding project setup functionality. It handles user input, directory creation, and file generation.

* `test_setup_project.py`: Test suite for the setup_project.py script. Contains unit tests for each function to ensure they work as expected.

## Function Descriptions

* `sanitize_project_name(name)`: Sanitizes the project name by replacing spaces with hyphens and removing special characters. This ensures that project directory names are terminal and filesystem friendly.

* `get_project_name()`: Prompts the user for a project name, sanitizes it, and informs the user if sanitization occurs. It will continue prompting until a valid name is provided.

* `get_project_description()`: Prompts the user for a brief project description and returns it.

* `create_project_directory(project_name)`: Creates the root project directory based on the provided project name. It checks if the directory already exists and exits with an error if it does. Returns the Path object for the created directory.

* `create_subdirectories(project_path)`: Creates the required subdirectories (memory-bank and .cursor) within the project directory. Returns the Path objects for the created subdirectories.

## Template Constants

* `PRODUCT_REQUIREMENTS_TEMPLATE`: Boilerplate content for the product-requirements-document.md file with placeholders for project_name and project_description.

* `TECH_STACK_TEMPLATE`: Boilerplate content for the tech-stack.md file with a placeholder for project_name.

* `IMPLEMENTATION_PLAN_TEMPLATE`: Boilerplate content for the implementation-plan.md file with a placeholder for project_name.

* `PROGRESS_TEMPLATE`: Boilerplate content for the progress.md file with a placeholder for project_name.

* `ARCHITECTURE_TEMPLATE`: Boilerplate content for the architecture.md file with a placeholder for project_name.

* `CURSOR_RULES_TEMPLATE`: Boilerplate content for the .cursor/rules file with predefined cursor rules based on the Vibe Coding methodology.

* `POST_EXECUTION_INSTRUCTIONS`: Instructions to display to the user after successfully creating the project structure, with placeholders for project_name.

## Project Structure

The script creates the following directory structure:

```
<project-name>/
├── memory-bank/
└── .cursor/
```

## Data Flow

1. The script prompts the user for a project name and description
2. It creates the root project directory with the provided name
3. It creates the required subdirectories within the root directory

In the future implementations, it will:
1. Populate the subdirectories with required files
2. Generate boilerplate content for each file
3. Print instructions for next steps 