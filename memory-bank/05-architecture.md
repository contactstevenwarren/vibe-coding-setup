# System Architecture Document

**Project:** Vibe Coding Project Setup Script

## File/Component Index

* **vibe-coding-setup** - Main Python script file responsible for creating project structure (renamed from script.py)
* **memory-bank/** - Directory for project documentation templates
  * **product-requirements-document.md** - Template for product requirements
  * **tech-stack.md** - Template for technology stack documentation
  * **implementation-plan.md** - Template for implementation plan
  * **progress.md** - Template for tracking project progress
  * **architecture.md** - Template for system architecture documentation
* **.cursor/rules/** - Directory for Cursor IDE rules
  * **01-vibe-coding-intro.mdc** - Introduction to Vibe Coding methodology
  * **02-memory-bank-access.mdc** - Rules for memory bank access
  * **03-implementation-guidelines.mdc** - Implementation guidelines
  * **04-documentation.mdc** - Documentation rules
* **Formula/vibe-coding-setup.rb** - Homebrew formula for installation via Homebrew
* **LICENSE.md** - MIT license file
* **vibe-coding-README.md** - README file for the GitHub repository

## Functions

* `sanitize_project_name(name)` - Transforms project name into a filesystem-friendly format (converts spaces to hyphens, removes special characters)
* `get_project_name()` - Prompts user for project name with validation
* `get_project_description()` - Prompts user for project description
* `create_root_directory(sanitized_name)` - Creates the root project directory
* `create_subdirectories(root_dir)` - Creates required subdirectories 
* `create_memory_bank_files(root_dir, project_name, project_description)` - Creates and populates memory-bank files
* `create_cursor_rules(root_dir)` - Creates and populates Cursor rules files
* `print_post_execution_instructions(root_dir, project_name)` - Displays formatted instructions
* `main()` - Main execution function with argument parsing
* `handle_error(e, message)` - Handles exceptions with user-friendly error messages

## Project Structure

```
project-name/
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

## Data Flow

1. Command-line argument parsing (--version flag)
2. User input collection (project name, description)
3. Sanitization of project name
4. Directory structure creation
5. File creation with templated content
6. Post-execution instructions output

## Error Handling Strategy

The script implements comprehensive error handling to ensure robustness:

1. **Input Validation** - Ensures all user inputs meet required criteria before proceeding
2. **File System Error Handling** - Gracefully manages existing directories and permission issues
3. **Exception Handling** - Custom error handling with user-friendly messages
4. **Validation Feedback** - Provides immediate feedback when input requires sanitization

## Key Design Decisions

1. **Project Name Sanitization**
   * Converts spaces to hyphens
   * Removes special characters
   * Preserves original name for display in content
   * Provides feedback to user when sanitization occurs

2. **Template System**
   * Uses Python string formatting with named placeholders
   * Templates stored as constants for easy maintenance
   * Consistent formatting across all generated files

3. **File Organization**
   * Separation of memory-bank documentation from IDE configuration
   * Consistent naming conventions for all files
   * Logical directory structure that separates concerns

4. **Cursor Rules Implementation**
   * Multiple specialized rule files instead of a single file
   * MDC format with proper metadata
   * Progressive rule organization (01, 02, etc.)
   * Rules aligned with Vibe Coding methodology

5. **Code Organization**
   * Modular function design with single responsibilities
   * Clear separation between user interaction and file operations
   * Consistent error handling pattern throughout codebase
   * Comprehensive docstrings for all functions

6. **Installation Options**
   * Homebrew formula for easy installation on macOS and Linux
   * Command-line options with argument parsing
   * Version information accessible via --version flag
   * Executable script with shebang line for direct execution

## Execution Flow

1. Script execution begins
2. Command-line arguments processed
3. If --version flag is provided, version is displayed and script exits
4. User prompted for project name (with validation)
5. User prompted for project description
6. Project name sanitized if necessary
7. Root directory created
8. Subdirectories created
9. Memory-bank files created and populated
10. Cursor rules files created and populated
11. Post-execution instructions displayed
12. Script terminates successfully

## Distribution Strategy

1. **GitHub Repository**
   * Main code repository with README and LICENSE
   * Tagged releases for version control
   * Distributed under MIT license

2. **Homebrew Tap**
   * Custom Homebrew tap for easy installation
   * Formula defines dependencies and installation instructions
   * Automated testing ensures script works when installed

3. **Version Management**
   * Semantic versioning (MAJOR.MINOR.PATCH)
   * Version information stored in script
   * Version flag provides easy access to version information

## Future Enhancement Considerations

1. Command-line argument support for non-interactive execution
2. Custom template directory option
3. Configuration file support for advanced customization
4. Additional memory-bank template options
5. Integration with version control systems 