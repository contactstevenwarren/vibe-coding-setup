# Design Document: Vibe Coding Project Setup Script

**Version:** 1.2
**Date:** 2024-07-26

## 1. Introduction

This document outlines the design for a simple command-line script that automates the initial setup phase for a "Vibe Coding" project, based on the principles in `MANUAL-VIBE-CODING.md`, with a focus on general application development. The script creates the necessary directory structure, essential files containing instructions for LLM generation, and a **boilerplate `.cursor/rules` file**, preparing the user to proceed with the manual steps involving LLMs (like Gemini) and the Cursor IDE.

## 2. Goals

*   Simplify the initial project setup process for Vibe Coding for application development.
*   Create a consistent starting structure for projects using this methodology.
*   Provide clear instructions within generated files for using LLMs to populate them.
*   **Provide a basic set of Cursor rules based on the Vibe Coding guide.**
*   Reduce the manual effort of creating directories and initial placeholder/boilerplate files.

## 3. Non-Goals

*   Automate interactions with LLMs (Gemini, Claude, etc.).
*   Generate a *complete* or *project-specific* set of Cursor rules.
*   Generate complete Product Requirements Documents, Tech Stack recommendations, or Implementation Plans directly.

## 4. Script Functionality

### 4.1 User Interaction

The script will run interactively in the terminal and prompt the user for the following information:
1.  **Project Name:** The desired name for the root project folder (e.g., `my-cool-app`).
2.  **Brief Project Description:** A short (1-2 sentence) description of the application idea.

### 4.2 Directory Structure Creation

Based on the provided Project Name, the script will create the following directory structure:

```
<project-name>/
├── memory-bank/
└── .cursor/
    └── rules
```

### 4.3 File Creation and Instructional/Boilerplate Content

The script will create the following files within the structure, populating them with instructions or boilerplate content:

1.  **`<project-name>/memory-bank/01-product-design-document.md`**
    *   **Generated Content:**
        ```markdown
        # Product Requirements Document (PRD)

        **Project:** <Project Name>

        *Initial Description Provided During Setup:*
        > <User-provided description>

        ---
        **Instructions for Generation:**

        Use an LLM (like Gemini 2.5 Pro) to flesh out this PRD based on your initial description. Provide the initial description and ask the LLM to expand on it, defining core features, target audience, user stories, and any non-functional requirements.

        **Example Prompt for LLM:**
        "Based on the following initial description for my project '<Project Name>', please help me create a detailed Product Requirements Document (PRD).
        Initial Description: '<User-provided description>'
        Please include sections for: Overview, Core Features (with brief descriptions), Target Audience, User Stories (at least 3-5 examples), and Non-Functional Requirements (e.g., performance, security)."

        *(Delete these instructions once the PRD is generated)*
        ---
        ```
2.  **`<project-name>/memory-bank/02-tech-stack.md`**
    *   **Generated Content:**
        ```markdown
        # Tech Stack Recommendations

        **Project:** <Project Name>

        ---
        **Instructions for Generation:**

        Use an LLM (like Gemini 2.5 Pro) to recommend a suitable tech stack for your project. Provide the LLM with the content of your `01-product-design-document.md`. Ask for the simplest yet most robust stack possible for your requirements.

        **Example Prompt for LLM:**
        "Based on the attached Product Requirements Document (`01-product-design-document.md`) for my project '<Project Name>', please recommend the simplest yet most robust tech stack. Consider frontend, backend (if applicable), database, and any key libraries or frameworks. Explain the reasoning behind your choices."

        *(Attach or paste the content of `01-product-design-document.md` when prompting. Delete these instructions once the tech stack is defined)*
        ---
        ```
3.  **`<project-name>/memory-bank/03-implementation-plan.md`**
    *   **Generated Content:**
        ```markdown
        # Implementation Plan

        **Project:** <Project Name>

        ---
        **Instructions for Generation:**

        Use an LLM (like Gemini 2.5 Pro) to create a detailed, step-by-step implementation plan. Provide the LLM with both your `01-product-design-document.md` and `02-tech-stack.md`. Each step should be small, specific, testable, and focus on building the core functionality first.

        **Example Prompt for LLM:**
        "Based on the attached Product Requirements Document (`01-product-design-document.md`) and Tech Stack (`02-tech-stack.md`) for my project '<Project Name>', please generate a detailed, step-by-step implementation plan. Break down the core functionality into small, manageable steps. For each step, describe the task and suggest a simple test to verify its completion. Focus on the Minimum Viable Product (MVP) first."

        *(Attach or paste the content of both `.md` files when prompting. Delete these instructions once the plan is generated)*
        ---
        ```
4.  **`<project-name>/memory-bank/04-progress.md`**
    *   **Generated Content:**
        ```markdown
        # Project Progress Tracker

        **Project:** <Project Name>

        ---
        **Instructions for Use:**

        As you complete steps from the `03-implementation-plan.md` using your AI coding assistant (e.g., Claude in Cursor), document the completed step, the date, and any relevant details (like the commit hash) here. This helps track progress and provides context for future work.

        **Format:**
        *   **[YYYY-MM-DD] - Step X: [Description of Step Completed]** - (Commit: `[hash]`, Notes: [Optional notes])

        *(Delete these instructions before starting to log progress)*
        ---

        ## Completed Steps

        ```
5.  **`<project-name>/memory-bank/05-architecture.md`**
    *   **Generated Content:**
        ```markdown
        # System Architecture Overview

        **Project:** <Project Name>

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

        ```
6.  **`<project-name>/.cursor/rules`**
    *   **Generated Content:**
        ```yaml
        # Cursor Rules - Boilerplate from Vibe Coding Setup
        # IMPORTANT: Review, refine, and add rules specific to your project and tech stack!
        # Consider using the `/Generate Cursor Rules` command in Cursor after filling the memory bank.

        rules:
          - trigger: "Always"
            response: "Always read memory-bank/05-architecture.md before writing any code. Include entire database schema if applicable."
            enabled: true

          - trigger: "Always"
            response: "Always read memory-bank/01-product-design-document.md before writing any code."
            enabled: true

          - trigger: "Default"
            response: "After adding a major feature or completing a milestone, update memory-bank/05-architecture.md."
            enabled: true

          - trigger: "Default"
            response: "Emphasize modularity (multiple files) and avoid creating monolithic files."
            enabled: true

          # Add more rules below, especially for your specific tech stack (e.g., state management, API design, testing).
          # Example:
          # - trigger: "On File Save *.js"
          #   response: "Ensure code adheres to ESLint rules configured in the project."
          #   enabled: true
        ```

### 4.4 Post-Execution Instructions

After creating the files and folders, the script will print the following instructions to the console:

```
✅ Project '<Project Name>' structure created successfully!

Next Steps:

1.  **Open the project folder in Cursor:**
    cd <project-name>
    cursor .
2.  **Generate Memory Bank Content:**
    *   Open `memory-bank/01-product-design-document.md`. Follow the instructions inside to generate the content using an LLM (like Gemini 2.5 Pro).
    *   Open `memory-bank/02-tech-stack.md`. Follow the instructions inside, using your PRD, to generate the content.
    *   Open `memory-bank/03-implementation-plan.md`. Follow the instructions inside, using your PRD and tech stack, to generate the plan.
3.  **Review and Refine Cursor Rules:**
    *   Open `.cursor/rules`. A boilerplate file has been created based on the Vibe Coding guide.
    *   **Crucially:** Review these rules. Adjust triggers (e.g., "Always" vs "Default") as needed.
    *   Add rules specific to your chosen tech stack and project requirements.
    *   You can also use the `/Generate Cursor Rules` command in Cursor (Command Palette -> "Configure Rules for '.cursor'") to potentially add more rules based on your memory bank files, then merge/refine.
4.  **Start Coding with Claude:**
    *   Open `memory-bank/05-architecture.md` and `memory-bank/04-progress.md` and remove the initial instruction blocks.
    *   Use Claude Sonnet 3.7 in Cursor: Read all the documents in /memory-bank, is 03-implementation-plan.md clear? What are your questions to make it 100% clear for you?
    *   Claude Sonnet 3.7 Thinking in Cursor: Read all the documents in /memory-bank, and proceed with Step 1 of the implementation plan. I will run the tests. Do not start Step 2 until I validate the tests. Once I validate them, open 04-progress.md and document what you did for future developers. Then add any architectural insights to 05-architecture.md to explain what each file does. And finally use Git for version control (`git init`, `git add .`, `git commit -m "Initial setup"`).
    *   Continue workflow: Now go through all files in the memory-bank, read 04-progress.md to understand prior work, and proceed with Step 2. Do not start Step 3 until I validate the test. Repeat this process until the entire 03-implementation-plan.md is complete.


Happy Vibe Coding!
```

## 5. Technology

*   The script can be implemented in any common scripting language like Python, Node.js (JavaScript), or Bash. Python is recommended for its ease of use for file system operations and cross-platform compatibility.

## 6. Future Enhancements (Optional)

*   Add options for different application templates (e.g., Web App, API, CLI Tool).
*   Integrate basic Git initialization (`git init`).
*   Add linters or basic config files based on the chosen tech stack (though this increases complexity). 