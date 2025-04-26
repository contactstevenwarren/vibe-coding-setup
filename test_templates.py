#!/usr/bin/env python3

import unittest
from setup_project import (
    PRODUCT_REQUIREMENTS_TEMPLATE,
    TECH_STACK_TEMPLATE,
    IMPLEMENTATION_PLAN_TEMPLATE,
    PROGRESS_TEMPLATE,
    ARCHITECTURE_TEMPLATE,
    CURSOR_RULES_TEMPLATE,
    POST_EXECUTION_INSTRUCTIONS
)

class TestBoilerplateTemplates(unittest.TestCase):
    
    def test_template_placeholders(self):
        """Test that templates contain the expected placeholders."""
        # Test templates that should have project_name placeholder
        for template in [
            PRODUCT_REQUIREMENTS_TEMPLATE,
            TECH_STACK_TEMPLATE,
            IMPLEMENTATION_PLAN_TEMPLATE,
            PROGRESS_TEMPLATE,
            ARCHITECTURE_TEMPLATE,
            POST_EXECUTION_INSTRUCTIONS
        ]:
            self.assertIn("{project_name}", template, f"Template missing project_name placeholder: {template[:50]}...")
        
        # Test templates that should have project_description placeholder
        self.assertIn("{project_description}", PRODUCT_REQUIREMENTS_TEMPLATE)
    
    def test_content_integrity(self):
        """Test that templates contain expected content sections."""
        # Check for key phrases in each template
        self.assertIn("Product Requirements Document (PRD)", PRODUCT_REQUIREMENTS_TEMPLATE)
        self.assertIn("Tech Stack Recommendations", TECH_STACK_TEMPLATE)
        self.assertIn("Implementation Plan", IMPLEMENTATION_PLAN_TEMPLATE)
        self.assertIn("Project Progress Tracker", PROGRESS_TEMPLATE)
        self.assertIn("System Architecture Overview", ARCHITECTURE_TEMPLATE)
        self.assertIn("Cursor Rules - Boilerplate", CURSOR_RULES_TEMPLATE)
        self.assertIn("Project '{project_name}' structure created successfully!", POST_EXECUTION_INSTRUCTIONS)
    
    def test_template_formatting(self):
        """Test that templates can be correctly formatted with placeholders."""
        test_project = "test-project"
        test_description = "This is a test project"
        
        # Test formatting with project_name
        for template in [
            PRODUCT_REQUIREMENTS_TEMPLATE,
            TECH_STACK_TEMPLATE,
            IMPLEMENTATION_PLAN_TEMPLATE,
            PROGRESS_TEMPLATE,
            ARCHITECTURE_TEMPLATE,
            POST_EXECUTION_INSTRUCTIONS
        ]:
            formatted = template.format(project_name=test_project, project_description=test_description)
            self.assertIn(test_project, formatted)
            self.assertNotIn("{project_name}", formatted)
        
        # Test formatting with project_description
        formatted_prd = PRODUCT_REQUIREMENTS_TEMPLATE.format(
            project_name=test_project, 
            project_description=test_description
        )
        self.assertIn(test_description, formatted_prd)
        self.assertNotIn("{project_description}", formatted_prd)

if __name__ == "__main__":
    unittest.main() 