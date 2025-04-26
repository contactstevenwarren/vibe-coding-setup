#!/usr/bin/env python3

from pathlib import Path
import sys
import re

# Boilerplate Content Templates
PRODUCT_REQUIREMENTS_TEMPLATE = """# Product Requirements Document (PRD)

**Project:** {project_name}

*Initial Description Provided During Setup:*
> {project_description}

---
**Instructions for Generation:**

Use an LLM (like Gemini 2.5 Pro) to flesh out this PRD based on your initial description. Provide the initial description and ask the LLM to expand on it, defining core features, target audience, user stories, and any non-functional requirements.

**Example Prompt for LLM:**
"Based on the following initial description for my project '{project_name}', please help me create a detailed Product Requirements Document (PRD).
Initial Description: '{project_description}'
Please include sections for: Overview, Core Features (with brief descriptions), Target Audience, User Stories (at least 3-5 examples), and Non-Functional Requirements (e.g., performance, security)."

*(Delete these instructions once the PRD is generated)*
---
"""

TECH_STACK_TEMPLATE = """# Tech Stack Recommendations

**Project:** {project_name}

---
**Instructions for Generation:**

Use an LLM (like Gemini 2.5 Pro) to recommend a suitable tech stack for your project. Provide the LLM with the content of your `product-requirements-document.md`. Ask for the simplest yet most robust stack possible for your requirements.

**Example Prompt for LLM:**
"Based on the attached Product Requirements Document (`product-requirements-document.md`) for my project '{project_name}', please recommend the simplest yet most robust tech stack. Consider frontend, backend (if applicable), database, and any key libraries or frameworks. Explain the reasoning behind your choices."

*(Attach or paste the content of `product-requirements-document.md` when prompting. Delete these instructions once the tech stack is defined)*
---
"""

IMPLEMENTATION_PLAN_TEMPLATE = """# Implementation Plan

**Project:** {project_name}

---
**Instructions for Generation:**

Use an LLM (like Gemini 2.5 Pro) to create a detailed, step-by-step implementation plan. Provide the LLM with both your `product-requirements-document.md` and `tech-stack.md`. Each step should be small, specific, testable, and focus on building the core functionality first.

**Example Prompt for LLM:**
"Based on the attached Product Requirements Document (`product-requirements-document.md`) and Tech Stack (`tech-stack.md`) for my project '{project_name}', please generate a detailed, step-by-step implementation plan. Break down the core functionality into small, manageable steps. For each step, describe the task and suggest a simple test to verify its completion. Focus on the Minimum Viable Product (MVP) first."

*(Attach or paste the content of both `.md` files when prompting. Delete these instructions once the plan is generated)*
---
"""

PROGRESS_TEMPLATE = """# Project Progress Tracker

**Project:** {project_name}

---
**Instructions for Use:**

As you complete steps from the `implementation-plan.md` using your AI coding assistant (e.g., Claude in Cursor), document the completed step, the date, and any relevant details (like the commit hash) here. This helps track progress and provides context for future work.

**Format:**
*   **[YYYY-MM-DD] - Step X: [Description of Step Completed]** - (Commit: `[hash]`, Notes: [Optional notes])

*(Delete these instructions before starting to log progress)*
---

## Completed Steps

"""

ARCHITECTURE_TEMPLATE = """# System Architecture Overview

**Project:** {project_name}

---
**Instructions for Use:**

As your AI coding assistant (e.g., Claude in Cursor) creates files, components, database schemas, or important data structures, document their purpose and how they interact here. This serves as a living reference for both you and the AI. Update this regularly, especially after adding major features or making significant architectural changes.

**Example Sections:**
*   File/Component Index (`path/to/file.ext`: Purpose)
*   Data Structures / Schema (Database tables, API interfaces, key state objects)
*   Diagrams (Consider adding Mermaid diagrams later: `https://mermaid.js.org/`)

*(Delete these instructions before starting to document the architecture)*
---

## File/Component Index

## Data Structures / Schema

## Diagrams (Optional)

"""

CURSOR_RULES_TEMPLATE = """# Cursor Rules - Boilerplate from Vibe Coding Setup
# IMPORTANT: Review, refine, and add rules specific to your project and tech stack!
# Consider using the `/Generate Cursor Rules` command in Cursor after filling the memory bank.

rules:
  - trigger: "Always"
    response: "Always read memory-bank/architecture.md before writing any code. Include entire database schema if applicable."
    enabled: true

  - trigger: "Always"
    response: "Always read memory-bank/product-requirements-document.md before writing any code."
    enabled: true

  - trigger: "Default"
    response: "After adding a major feature or completing a milestone, update memory-bank/architecture.md."
    enabled: true

  - trigger: "Default"
    response: "Emphasize modularity (multiple files) and avoid creating monolithic files."
    enabled: true

  # Add more rules below, especially for your specific tech stack (e.g., state management, API design, testing).
  # Example:
  # - trigger: "On File Save *.js"
  #   response: "Ensure code adheres to ESLint rules configured in the project."
  #   enabled: true
"""

POST_EXECUTION_INSTRUCTIONS = """✅ Project '{project_name}' structure created successfully!

Next Steps:

1.  **Open the project folder in Cursor:**
    cd {project_name}
    cursor .
2.  **Generate Memory Bank Content:**
    *   Open `memory-bank/product-requirements-document.md`. Follow the instructions inside to generate the content using an LLM (like Gemini 2.5 Pro).
    *   Open `memory-bank/tech-stack.md`. Follow the instructions inside, using your PRD, to generate the content.
    *   Open `memory-bank/implementation-plan.md`. Follow the instructions inside, using your PRD and tech stack, to generate the plan.
3.  **Review and Refine Cursor Rules:**
    *   Open `.cursor/rules`. A boilerplate file has been created based on the Vibe Coding guide.
    *   **Crucially:** Review these rules. Adjust triggers (e.g., "Always" vs "Default") as needed.
    *   Add rules specific to your chosen tech stack and project requirements.
    *   You can also use the `/Generate Cursor Rules` command in Cursor (Command Palette -> "Configure Rules for '.cursor'") to potentially add more rules based on your memory bank files, then merge/refine.
4.  **Start Coding with Claude:**
    *   Open `memory-bank/architecture.md` and `memory-bank/progress.md` and remove the initial instruction blocks.
    *   Use Claude Sonnet 3.7 in Cursor: Read all the documents in /memory-bank, is implementation-plan.md clear? What are your questions to make it 100% clear for you?
    *   Claude Sonnet 3.7 Thinking in Cursor: Read all the documents in /memory-bank, and proceed with Step 1 of the implementation plan. I will run the tests. Do not start Step 2 until I validate the tests. Once I validate them, open progress.md and document what you did for future developers. Then add any architectural insights to architecture.md to explain what each file does. And finally use Git for version control (`git init`, `git add .`, `git commit -m "Initial setup"`).
    *   Continue workflow: Now go through all files in the memory-bank, read progress.md to understand prior work, and proceed with Step 2. Do not start Step 3 until I validate the test. Repeat this process until the entire implementation-plan.md is complete.


Happy Vibe Coding!
"""

def sanitize_project_name(name):
    """
    Sanitize project name by replacing spaces with hyphens and removing special characters.
    This helps avoid issues with file paths and terminal commands.
    """
    # Replace spaces with hyphens
    sanitized = name.replace(" ", "-")
    # Remove any characters that aren't alphanumeric, hyphens, or underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '', sanitized)
    # Ensure the name doesn't start or end with a hyphen
    sanitized = sanitized.strip('-')
    
    return sanitized

def get_project_name():
    """Prompt the user for a project name and validate it."""
    while True:
        project_name = input("Enter project name: ").strip()
        if not project_name:
            print("Error: Project name cannot be empty. Please try again.")
            continue
            
        sanitized_name = sanitize_project_name(project_name)
        if sanitized_name != project_name:
            print(f"Project name sanitized to '{sanitized_name}' for compatibility.")
        
        return sanitized_name

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

def create_memory_bank_files(memory_bank_path, project_name, project_description):
    """
    Create and populate the required files in the memory-bank directory.
    
    Args:
        memory_bank_path: Path object for the memory-bank directory
        project_name: Name of the project
        project_description: Description of the project
    """
    # Define the files to create and their content templates
    files_to_create = {
        "product-requirements-document.md": PRODUCT_REQUIREMENTS_TEMPLATE,
        "tech-stack.md": TECH_STACK_TEMPLATE,
        "implementation-plan.md": IMPLEMENTATION_PLAN_TEMPLATE,
        "progress.md": PROGRESS_TEMPLATE,
        "architecture.md": ARCHITECTURE_TEMPLATE
    }
    
    created_files = []
    
    # Create each file with the appropriate content
    for filename, template in files_to_create.items():
        file_path = memory_bank_path / filename
        
        try:
            # Format the template with project details
            content = template.format(
                project_name=project_name,
                project_description=project_description
            )
            
            # Write the content to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Created file: {file_path}")
            created_files.append(file_path)
        except Exception as e:
            print(f"Error creating {filename}: {e}")
            
    return created_files

if __name__ == "__main__":
    print("Vibe Coding Project Setup Script")
    project_name = get_project_name()
    project_description = get_project_description()
    project_path = create_project_directory(project_name)
    memory_bank_path, cursor_path = create_subdirectories(project_path)
    
    # Create memory-bank files
    memory_bank_files = create_memory_bank_files(memory_bank_path, project_name, project_description)
    
    print(f"Project name: {project_name}")
    print(f"Project description: {project_description}")
    print(f"Project directory: {project_path}")
    # Later steps will add more functionality here 