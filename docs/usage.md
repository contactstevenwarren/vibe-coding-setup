# Usage Guide

This guide provides detailed instructions on how to use the Vibe Coding Project Setup Script.

## Prerequisites

- Python 3.6 or higher
- No additional dependencies required

## Running the Script

To run the script, navigate to the project directory and execute:

```bash
python setup_project.py
```

## Interactive Prompts

The script will guide you through the setup process:

1. **Project Name**: 
   - Enter a name for your project
   - The name will be sanitized for filesystem compatibility (spaces converted to hyphens, special characters removed)
   - You'll be notified if sanitization occurs
   - Both the original name (for content) and sanitized name (for directories) are saved

2. **Project Description**:
   - Enter a brief description of your project
   - This will be used in the generated documentation templates

## Generated Structure

After providing the inputs, the script creates:

1. **Root Project Directory**:
   - Named after your sanitized project name
   - Created in the current working directory

2. **Subdirectories**:
   - `memory-bank/` - Contains project documentation
   - `.cursor/rules/` - Contains Cursor IDE rules

3. **Memory Bank Files**:
   - `product-requirements-document.md` - Template for defining project requirements
   - `tech-stack.md` - Template for documenting technology choices
   - `implementation-plan.md` - Template for planning implementation steps
   - `progress.md` - Template for tracking project progress
   - `architecture.md` - Template for documenting system architecture

4. **Cursor Rule Files**:
   - Multiple MDC-formatted rule files in the `.cursor/rules/` directory
   - Each file contains metadata and focuses on a specific aspect of the Vibe Coding methodology

## Post-Execution

After creating the project structure, the script prints detailed instructions:

1. **Opening the Project**:
   - How to open the project in Cursor IDE

2. **Generating Content**:
   - How to use Claude to populate the memory bank files
   - Step-by-step prompts for working with each file

3. **Using Cursor Rules**:
   - How to review and refine the generated Cursor rules
   - How to add project-specific rules

4. **Starting Development**:
   - How to begin implementing your project following the Vibe Coding methodology

## Error Handling

The script includes robust error handling:

- Validates user input
- Checks for existing directories
- Provides clear error messages
- Gracefully exits if critical errors occur

## Example Session

```
Vibe Coding Project Setup Script
Enter a project name: My Awesome Project
The project name has been sanitized from "My Awesome Project" to "my-awesome-project" for filesystem compatibility.
Enter a brief project description: A web application for tracking daily habits and goals.
Created project directory: /path/to/my-awesome-project
Created subdirectory: /path/to/my-awesome-project/memory-bank
Created subdirectory: /path/to/my-awesome-project/.cursor
Created file: /path/to/my-awesome-project/memory-bank/product-requirements-document.md
Created file: /path/to/my-awesome-project/memory-bank/tech-stack.md
Created file: /path/to/my-awesome-project/memory-bank/implementation-plan.md
Created file: /path/to/my-awesome-project/memory-bank/progress.md
Created file: /path/to/my-awesome-project/memory-bank/architecture.md
Created rule file: /path/to/my-awesome-project/.cursor/rules/01-vibe-coding-intro.mdc
Created rule file: /path/to/my-awesome-project/.cursor/rules/02-memory-bank-access.mdc
Created rule file: /path/to/my-awesome-project/.cursor/rules/03-implementation-guidelines.mdc
Created rule file: /path/to/my-awesome-project/.cursor/rules/04-documentation.mdc
Project name: My Awesome Project
Sanitized directory name: my-awesome-project
Project description: A web application for tracking daily habits and goals.
Project directory: /path/to/my-awesome-project

--------------------------------------------------------------------------------
✅ Project 'My Awesome Project' structure created successfully!

...
(post-execution instructions)
...
-------------------------------------------------------------------------------- 