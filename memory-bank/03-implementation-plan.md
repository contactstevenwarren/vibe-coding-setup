Okay, here is a detailed, step-by-step implementation plan for the "Vibe Coding Project Setup Script" based on the provided `01-product-design-document.md` and `02-tech-stack.md`.

**Project:** Vibe Coding Project Setup Script
**Tech Stack:** Python 3 (Standard Library Only)

---

## Implementation Plan (MVP)

**Goal:** Create a Python script that prompts the user for a project name and description, then generates the specified directory structure and boilerplate files with instructional content.

**Phase 1: Core Script Setup & User Input**

1.  **Step 1: Initialize Script File**
    *   **Task:** Create the main Python script file (e.g., `setup_project.py`). Add basic structure like `if __name__ == "__main__":`. Import the `pathlib` module.
    *   **Test:** Run `python setup_project.py` from the terminal. It should execute without errors (and do nothing yet).

2.  **Step 2: Get Project Name**
    *   **Task:** Implement code within the script to prompt the user for the "Project Name" using the `input()` function. Store the result in a variable (e.g., `project_name`). Add validation to ensure the name is not empty.
    *   **Test:** Run the script. Enter a project name when prompted. Print the `project_name` variable to the console to verify it was captured correctly. Test with empty input to ensure validation works.

3.  **Step 3: Get Project Description**
    *   **Task:** Implement code to prompt the user for a "Brief Project Description" using `input()`. Store the result in a variable (e.g., `project_description`).
    *   **Test:** Run the script. Enter a name and description. Print both variables to verify capture.

**Phase 2: Directory and File Structure Creation**

4.  **Step 4: Create Root Project Directory**
    *   **Task:** Use `pathlib.Path` to represent the desired project path based on `project_name`. Use `Path.mkdir()` to create the directory. Include error handling: check if the directory already exists using `Path.exists()` and print an informative error message/exit if it does.
    *   **Test:** Run the script with a new project name (e.g., `test-app`). Verify the `test-app` directory is created. Run the script again with the *same* name. Verify the script prints an error and exits without crashing.

5.  **Step 5: Create Subdirectories (`memory-bank`, `.cursor`)**
    *   **Task:** Inside the root project directory path, create the `memory-bank` and `.cursor` subdirectories using `Path.mkdir(parents=True, exist_ok=True)`. `exist_ok=True` is safe here as we've already checked the root.
    *   **Test:** Run the script with a new project name. Verify that `memory-bank` and `.cursor` directories are created inside the root project directory.

**Phase 3: Boilerplate Content Generation**

6.  **Step 6: Define Boilerplate Content Templates**
    *   **Task:** Store the multi-line boilerplate content for each target file (`01-product-design-document.md`, `02-tech-stack.md`, `03-implementation-plan.md`, `04-progress.md`, `05-architecture.md`, `.cursor/rules`) as string constants (e.g., using triple quotes `"""..."""`) within the Python script. Use Python-style placeholders like `{project_name}` and `{project_description}` within these strings for easy formatting (e.g., using f-strings or `.format()`), even if the source `01-product-design-document.md` uses `<...>` for illustration.
    *   **Test:** Internal step. Correctness will be verified in the next steps when files are written.

7.  **Step 7: Create and Populate `memory-bank` Files**
    *   **Task:** For each of the five `.md` files destined for the `memory-bank` directory:
        *   Construct the full `pathlib.Path` object for the file (e.g., `root_path / "memory-bank" / "01-product-design-document.md"`).
        *   Use f-strings or the `.format()` method on the corresponding boilerplate string template to insert the captured `project_name` and `project_description` variables.
        *   Open the file path in write mode (`'w'`, encoding='utf-8') using a `with` statement.
        *   Write the formatted content to the file.
    *   **Test:** Run the script. Navigate into the created `project-name/memory-bank/` directory. Open each `.md` file and verify:
        *   The file exists.
        *   The content matches the boilerplate from `01-product-design-document.md`.
        *   `<Project Name>` has been replaced with the actual project name entered.
        *   `<User-provided description>` has been replaced with the actual description entered (in `01-product-design-document.md`).

8.  **Step 8: Create and Populate `.cursor/rules` File**
    *   **Task:**
        *   Construct the full `pathlib.Path` for `<project-name>/.cursor/rules`.
        *   Get the corresponding boilerplate string template (which doesn't need formatting).
        *   Open the file path in write mode (`'w'`, encoding='utf-8') using a `with` statement.
        *   Write the content to the file.
    *   **Test:** Run the script. Navigate into the created `project-name/.cursor/` directory. Open the `rules` file and verify its content matches the boilerplate YAML from `01-product-design-document.md`.

**Phase 4: Final Output and Refinement**

9.  **Step 9: Print Post-Execution Instructions**
    *   **Task:** Define the multi-line post-execution instructions string (from `01-product-design-document.md`) within the script. Use f-strings or `.format()` to insert the actual `project_name` into the instructions where `<Project Name>` appears. Use `print()` to display these formatted instructions to the console after all files/directories have been created successfully.
    *   **Test:** Run the script successfully. Verify the complete set of "Next Steps" instructions is printed to the console, and `<Project Name>` placeholders have been correctly substituted.

10. **Step 10: Code Cleanup and Comments**
    *   **Task:** Review the script for clarity. Add comments where the logic isn't immediately obvious. Ensure consistent formatting. Group related constants (like boilerplate text) together. Structure the main execution flow logically.
    *   **Test:** Read through the code. Does it make sense? Are file operations handled safely (e.g., using `with open(...)`)? Is the error handling for existing directories clear?

---

This plan breaks down the script creation into manageable, testable steps, focusing on delivering the core MVP functionality first. 