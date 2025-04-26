# Vibe Coding Project Setup Script

A Python utility for initializing a project structure following the Vibe Coding methodology.

## Overview

The Vibe Coding Project Setup Script automates the creation of a standardized project structure, designed to facilitate development with LLMs (Large Language Models) like Claude in the Cursor IDE. It creates the necessary directory structure, documentation templates, and IDE configuration files for a Vibe Coding project.

## Features

- Interactive prompts for project name and description
- Automatic creation of project directory structure
- Generation of memory-bank documentation templates
- Creation of Cursor IDE rules files in MDC format
- Support for project name sanitization for filesystem compatibility
- Comprehensive error handling
- Detailed post-execution instructions

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd vibe-coding-setup
```

No additional dependencies are required—the script uses only the Python standard library.

## Usage

Run the script using Python:

```bash
python setup_project.py
```

The script will:

1. Prompt you for a project name (will be sanitized if needed)
2. Prompt you for a project description
3. Create the project directory structure
4. Populate the structure with template files
5. Display instructions for next steps

## Project Structure

The script creates the following structure:

```
{project_name}/
├── memory-bank/
│   ├── product-requirements-document.md
│   ├── tech-stack.md
│   ├── implementation-plan.md
│   ├── progress.md
│   └── architecture.md
└── .cursor/
    └── rules/
        ├── 01-vibe-coding-intro.mdc
        ├── 02-memory-bank-access.mdc
        ├── 03-implementation-guidelines.mdc
        └── 04-documentation.mdc
```

## Memory Bank Files

- **product-requirements-document.md**: Template for defining project requirements
- **tech-stack.md**: Template for documenting technology choices
- **implementation-plan.md**: Template for planning implementation steps
- **progress.md**: Template for tracking project progress
- **architecture.md**: Template for documenting system architecture

## Cursor Rules

The script creates MDC-formatted rule files for the Cursor IDE that implement the Vibe Coding methodology:

- **01-vibe-coding-intro.mdc**: Introduction to Vibe Coding principles
- **02-memory-bank-access.mdc**: Rules for accessing the memory bank
- **03-implementation-guidelines.mdc**: Implementation guidelines
- **04-documentation.mdc**: Documentation rules

## Workflow

After running the script:

1. Open the project in Cursor IDE
2. Use an LLM like Claude to generate content for memory-bank files
3. Review and refine the Cursor rules as needed
4. Begin implementing your project following the Vibe Coding methodology

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE) 