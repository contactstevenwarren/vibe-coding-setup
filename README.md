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

## Quick Start

Run the script using Python:

```bash
python setup_project.py
```

Follow the prompts to create your project.

## Documentation

For detailed documentation, please see the [docs directory](docs/README.md).

## Project Structure Created

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

## License

[MIT License](LICENSE) 