# Vibe Coding Setup

This project is inspired by the [Ultimate Guide to Vibe Coding by Nicolas Zullo](https://github.com/EnzeD/vibe-coding). The Vibe Coding Project Setup Script automates the creation of a standardized project structure, designed to facilitate development with LLMs (Large Language Models) like Claude in the Cursor IDE. It creates the necessary directory structure, documentation templates, and IDE configuration files for a Vibe Coding project.

## What is Vibe Coding?

Vibe Coding is a methodology for working effectively with Large Language Models (LLMs) like Claude and Gemini in the development process. It emphasizes creating a structured "memory bank" of documentation that can be referenced by the LLM to improve context and consistency throughout development.

## Features

- Creates a project directory with a consistent structure
- Sets up a memory-bank directory with template files for:
  - Product Requirements Document
  - Tech Stack Recommendations
  - Implementation Plan
  - Progress Tracker
  - Architecture Documentation
- Configures Cursor IDE with rules for the Vibe Coding methodology
- Guides users through the setup process with clear instructions

## Installation

### Via Homebrew (macOS and Linux)

```bash
# Add the tap repository
brew tap contactstevenwarren/vibe-coding

# Install the script
brew install vibe-coding-setup

# Verify installation
vibe-coding-setup --version
```

### Manual Installation

1. Clone this repository
2. Make the script executable: `chmod +x vibe-coding-setup`
3. Optionally, move the script to a directory in your PATH

## Usage

Simply run the `vibe-coding-setup` command:

```bash
vibe-coding-setup
```

Follow the prompts to enter your project name and description. The script will:

1. Create a new project directory with the sanitized name
2. Set up the memory-bank directory with template files
3. Configure Cursor IDE rules
4. Provide instructions for next steps

## Project Structure

The script creates the following directory structure:

```
project-name/
├── memory-bank/
│   ├── 01-product-design-document.md
│   ├── 02-tech-stack.md
│   ├── 03-implementation-plan.md
│   ├── 04-progress.md
│   └── 05-architecture.md
└── .cursor/
    └── rules/
        ├── architecture.mdc
        ├── requirements.mdc
        ├── update_architecture.mdc
        ├── update_progress.mdc
        ├── validation_workflow.mdc
        ├── modularity.mdc
        └── readme.mdc
```

## License

MIT License 