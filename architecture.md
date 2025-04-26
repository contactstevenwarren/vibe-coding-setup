# System Architecture Document

**Project:** Vibe Coding Project Setup Script

## File/Component Index

* **script.py** - Main Python script file responsible for creating project structure
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

## Functions

* `sanitize_project_name(name)` - Transforms project name into a filesystem-friendly format (converts spaces to hyphens, removes special characters)
* `get_project_name()` - Prompts user for project name with validation
* `get_project_description()` - Prompts user for project description
* `create_root_directory(sanitized_name)` - Creates the root project directory
* `create_subdirectories(root_dir)` - Creates required subdirectories 
* `create_memory_bank_files(root_dir, project_name, project_description)` - Creates and populates memory-bank files
* `create_cursor_rules(root_dir)` - Creates and populates Cursor rules files
* `print_post_execution_instructions(root_dir, project_name)` - Displays formatted instructions
* `main()` - Main execution function
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

1. User input collection (project name, description)
2. Sanitization of project name
3. Directory structure creation
4. File creation with templated content
5. Post-execution instructions output

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

## Execution Flow

1. Script execution begins
2. User prompted for project name (with validation)
3. User prompted for project description
4. Project name sanitized if necessary
5. Root directory created
6. Subdirectories created
7. Memory-bank files created and populated
8. Cursor rules files created and populated
9. Post-execution instructions displayed
10. Script terminates successfully

## Future Enhancement Considerations

1. Command-line argument support for non-interactive execution
2. Custom template directory option
3. Configuration file support for advanced customization
4. Additional memory-bank template options
5. Integration with version control systems 