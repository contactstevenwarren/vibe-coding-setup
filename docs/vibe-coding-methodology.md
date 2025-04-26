# Vibe Coding Methodology

Vibe Coding is a structured approach to developing software projects with large language models (LLMs) like Claude and Gemini. This methodology emphasizes planning, documentation, and incremental development to create maintainable, high-quality software.

## Core Principles

1. **Planning First**: Detailed planning before coding prevents technical debt and architectural problems.
2. **Documentation-Driven**: Documentation precedes and guides implementation.
3. **Memory Bank**: A central repository of project knowledge for LLMs to reference.
4. **Incremental Development**: Small, testable steps with validation at each stage.
5. **Structured Rules**: Clear rules for LLMs to maintain consistency and best practices.
6. **Human Validation**: Regular human review and direction at key decision points.

## The Memory Bank

The memory bank is a collection of documentation files that serve as the project's knowledge base:

1. **Product Requirements Document (PRD)**: Defines what the project should accomplish, core features, target audience, and constraints.
2. **Tech Stack**: Documents technology choices and rationale.
3. **Implementation Plan**: Step-by-step breakdown of development tasks with validation criteria.
4. **Progress Tracker**: Documents completed implementation steps and milestones.
5. **Architecture Document**: Describes system components, file organization, and interactions.

## Workflow

### Setup Phase

1. **Define Product Requirements**: Create a detailed PRD with features, user stories, and non-functional requirements.
2. **Select Tech Stack**: Choose appropriate technologies based on project requirements.
3. **Create Implementation Plan**: Break down development into small, testable steps.
4. **Configure Cursor Rules**: Set up rules for the LLM to follow during development.

### Development Phase

1. **Step Execution**: The LLM (e.g., Claude) implements a single step from the implementation plan.
2. **Validation**: The developer validates the implementation meets requirements.
3. **Documentation Update**: The LLM updates progress tracking and architecture documentation.
4. **Review**: The developer reviews changes and provides feedback.
5. **Iteration**: Repeat for each implementation step.

## Rules in Vibe Coding

Cursor rules guide the LLM's behavior during development:

1. **Always Rules**: Critical guidelines that must be followed before any code generation, such as:
   - Always reading architecture documentation before writing code
   - Always reading product requirements before writing code

2. **Default Rules**: Best practices that should generally be followed:
   - Updating documentation after completing milestones
   - Following specific coding patterns or architecture principles

3. **Manual Rules**: Additional guidelines that require human judgment to apply

## Benefits of Vibe Coding

1. **Improved Project Structure**: Prevents monolithic codebases through planned architecture
2. **Maintainability**: Well-documented systems are easier to maintain and extend
3. **Contextual Understanding**: LLMs maintain context across multiple sessions
4. **Consistency**: Rules ensure consistent coding practices
5. **Incremental Progress**: Step-by-step approach prevents overwhelming complexity
6. **Human-AI Collaboration**: Combines AI's code generation with human direction and validation

## Implementation with Different LLMs

- **Claude**: Excels at following structured rules and implementing detailed steps
- **Gemini**: Useful for broader planning and architecture design due to larger context window
- **Mixed Approach**: Use Gemini for planning and Claude for implementation

## Common Pitfalls to Avoid

1. **Skipping Documentation**: Shortcuts in documentation lead to inconsistent implementation
2. **Monolithic Design**: Failing to emphasize modularity leads to coupled, hard-to-maintain code
3. **Vague Implementation Steps**: Poorly defined steps result in misaligned implementation
4. **Insufficient Testing**: Each step should include validation criteria
5. **Ignoring Rules**: Rules ensure consistency and best practices

## Getting Started

To begin using the Vibe Coding methodology:

1. Set up a project structure using the Vibe Coding Setup Script
2. Populate the memory bank with project-specific information
3. Configure and review Cursor rules
4. Follow the incremental development workflow