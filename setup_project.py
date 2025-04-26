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

# Update template constants for Cursor rules
CURSOR_RULES_ARCHITECTURE = """---
description: Enforce reading architecture documentation
type: Always
---

Always read memory-bank/architecture.md before writing any code. Include entire database schema if applicable.
"""

CURSOR_RULES_REQUIREMENTS = """---
description: Enforce reading requirements documentation
type: Always
---

Always read memory-bank/product-requirements-document.md before writing any code.
"""

CURSOR_RULES_UPDATE_ARCHITECTURE = """---
description: Remember to update architecture documentation
type: Default
---

After adding a major feature or completing a milestone, update memory-bank/architecture.md.
"""

CURSOR_RULES_UPDATE_PROGRESS = """---
description: Remember to update progress tracker
type: Default
---

After completing a milestone or implementation step, update memory-bank/progress.md with details about what was accomplished.
"""

CURSOR_RULES_VALIDATION_WORKFLOW = """---
description: Implementation step validation workflow
type: Always
---

For each implementation step from the implementation plan:

1. Complete the implementation for the current step only
2. Ask the user to validate and confirm before proceeding to the next step
3. Once validated:
   - Update memory-bank/progress.md with details about the completed step
   - Update memory-bank/architecture.md if the step involved new components or structures
   - Commit changes to git with a descriptive message
4. Only after validation, proceed to the next implementation step
"""

CURSOR_RULES_MODULARITY = """---
description: Enforce code modularity
type: Default
---

Emphasize modularity (multiple files) and avoid creating monolithic files.
"""

CURSOR_RULES_README = """---
description: Guide for adding more rules
type: Manual
---

# Add more rules below, especially for your specific tech stack
Examples:
- State management patterns
- API design principles
- Testing requirements
- Styling conventions

Use the `/Generate Cursor Rules` command in Cursor to generate more rules based on your memory bank files.
"""

POST_EXECUTION_INSTRUCTIONS = """✅ Project '{project_name}' structure created successfully!

Next Steps:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. OPEN THE PROJECT FOLDER IN CURSOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    $ cd {directory_name}
    $ cursor .

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. GENERATE MEMORY BANK CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    • Open `memory-bank/product-requirements-document.md` and follow the instructions
    • Open `memory-bank/tech-stack.md` and follow the instructions
    • Open `memory-bank/implementation-plan.md` and follow the instructions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. REVIEW AND REFINE CURSOR RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    • The `.cursor/rules` directory contains MDC rule files based on Vibe Coding guide
    • Review these rules in the Cursor editor 
    • Add rules specific to your chosen tech stack
    • Use `/Generate Cursor Rules` command for additional rules

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. START CODING WITH CLAUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    • First, select Claude Sonnet 3.7 Thinking in Cursor
    
    • Initial prompt (copy & paste this):
      
      Read all the documents in /memory-bank, and proceed with Step 1 of the implementation plan. I will run the tests. Do not start Step 2 until I validate the tests. Once I validate them, open progress.md and document what you did for future developers. Then add any architectural insights to architecture.md to explain what each file does.
    
    • After validating Step 1 and committing your changes, continue with (copy & paste):
      
      Now go through all files in the memory-bank, read progress.md to understand prior work, and proceed with Step 2. Do not start Step 3 until I validate the test.
    
    • Repeat this process for each step until the entire implementation-plan.md is complete


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
            print(f"Project name sanitized to '{sanitized_name}' for directory and file paths.")
        
        # Return both the original and sanitized names
        return project_name, sanitized_name

def get_project_description():
    """Prompt the user for a project description."""
    return input("Enter a brief project description: ").strip()

def create_project_directory(sanitized_project_name):
    """Create the root project directory. Exit if it already exists."""
    project_path = Path.cwd() / sanitized_project_name
    
    if project_path.exists():
        print(f"Error: Directory '{sanitized_project_name}' already exists. Please choose a different name.")
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

def create_memory_bank_files(memory_bank_path, original_project_name, project_description):
    """
    Create and populate the required files in the memory-bank directory.
    
    Args:
        memory_bank_path: Path object for the memory-bank directory
        original_project_name: Original human-readable project name for file content
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
            # Format the template with project details, using the original name for content
            content = template.format(
                project_name=original_project_name,
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

def create_cursor_rules_files(cursor_path):
    """
    Create and populate the .cursor/rules directory with MDC rule files.
    
    Args:
        cursor_path: Path object for the .cursor directory
    """
    # Create rules directory if it doesn't exist
    rules_dir = cursor_path / "rules"
    if not rules_dir.exists():
        rules_dir.mkdir(exist_ok=True)
    
    # Define the rules to create
    rules_to_create = {
        "architecture.mdc": CURSOR_RULES_ARCHITECTURE,
        "requirements.mdc": CURSOR_RULES_REQUIREMENTS,
        "update_architecture.mdc": CURSOR_RULES_UPDATE_ARCHITECTURE,
        "update_progress.mdc": CURSOR_RULES_UPDATE_PROGRESS,
        "validation_workflow.mdc": CURSOR_RULES_VALIDATION_WORKFLOW,
        "modularity.mdc": CURSOR_RULES_MODULARITY,
        "readme.mdc": CURSOR_RULES_README
    }
    
    created_files = []
    
    # Create each rule file with the appropriate content
    for filename, content in rules_to_create.items():
        file_path = rules_dir / filename
        
        try:
            # Write the content to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Created rule file: {file_path}")
            created_files.append(file_path)
        except Exception as e:
            print(f"Error creating {filename}: {e}")
            
    return created_files

def print_post_execution_instructions(original_project_name, sanitized_project_name):
    """
    Format and print post-execution instructions to the user.
    
    Args:
        original_project_name: Original human-readable name of the project
        sanitized_project_name: Sanitized name of the project used for directory
    """
    # Format the instructions with the project name and directory name
    instructions = POST_EXECUTION_INSTRUCTIONS.format(
        project_name=original_project_name,
        directory_name=sanitized_project_name
    )
    
    # Print the formatted instructions
    print("\n" + "-" * 80)
    print(instructions)
    print("-" * 80 + "\n")

if __name__ == "__main__":
    print("Vibe Coding Project Setup Script")
    original_project_name, sanitized_project_name = get_project_name()
    project_description = get_project_description()
    project_path = create_project_directory(sanitized_project_name)
    memory_bank_path, cursor_path = create_subdirectories(project_path)
    
    # Create memory-bank files with the original project name for content
    memory_bank_files = create_memory_bank_files(memory_bank_path, original_project_name, project_description)
    
    # Create .cursor/rules files
    cursor_rules_files = create_cursor_rules_files(cursor_path)
    
    print(f"Project name: {original_project_name}")
    print(f"Sanitized directory name: {sanitized_project_name}")
    print(f"Project description: {project_description}")
    print(f"Project directory: {project_path}")
    
    # Print post-execution instructions
    print_post_execution_instructions(original_project_name, sanitized_project_name) 