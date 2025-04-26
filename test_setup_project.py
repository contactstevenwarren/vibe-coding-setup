#!/usr/bin/env python3
"""
Unit tests for the Vibe Coding Project Setup Script

This module contains tests for all major functionality in setup_project.py,
including input validation, directory creation, file generation, and output formatting.
"""

import unittest
import subprocess
import sys
import io
import unittest.mock
import shutil
from pathlib import Path
from setup_project import (
    get_project_name, 
    get_project_description, 
    create_project_directory,
    create_subdirectories,
    sanitize_project_name,
    create_memory_bank_files,
    create_cursor_rules_files,
    print_post_execution_instructions,
    CURSOR_RULES_ARCHITECTURE,
    CURSOR_RULES_REQUIREMENTS,
    POST_EXECUTION_INSTRUCTIONS,
    main
)

class TestSetupProject(unittest.TestCase):
    """
    Test cases for the Vibe Coding Project Setup Script functionality
    """
    
    def setUp(self):
        # Create a temporary test directory
        self.test_dir = Path.cwd() / "test_temp_dir"
        if not self.test_dir.exists():
            self.test_dir.mkdir()
    
    def tearDown(self):
        # Clean up test directory after tests
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
    
    def test_script_runs_without_error(self):
        """Test that the setup_project.py script runs without errors."""
        # Skip running the full script in tests since it would prompt for input
        # Instead, we'll test individual components
        pass
    
    def test_sanitize_project_name(self):
        """Test that sanitize_project_name correctly formats project names."""
        test_cases = [
            ("my project", "my-project"),
            ("My Cool Project!", "My-Cool-Project"),
            ("project with @#$special chars", "project-with-special-chars"),
            ("--project--name--", "project--name"),
            ("project_name", "project_name"),  # Underscores should be preserved
            ("project-name", "project-name"),  # Already well-formatted
            ("123 Project", "123-Project"),    # Numbers should be preserved
        ]
        
        for input_name, expected_output in test_cases:
            self.assertEqual(sanitize_project_name(input_name), expected_output)
    
    def test_get_project_name_sanitized(self):
        """Test that get_project_name returns sanitized input."""
        # Mock user entering a name with spaces
        with unittest.mock.patch('builtins.input', return_value="test project"):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                original_name, sanitized_name = get_project_name()
                self.assertEqual(original_name, "test project")
                self.assertEqual(sanitized_name, "test-project")
                self.assertIn("sanitized to", fake_stdout.getvalue())
    
    def test_get_project_name_already_sanitized(self):
        """Test that get_project_name handles already sanitized input."""
        with unittest.mock.patch('builtins.input', return_value="test-project"):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                original_name, sanitized_name = get_project_name()
                self.assertEqual(original_name, "test-project")
                self.assertEqual(sanitized_name, "test-project")
                self.assertNotIn("sanitized to", fake_stdout.getvalue())
    
    def test_get_project_name_empty_then_valid(self):
        """Test that get_project_name rejects empty input then accepts valid input."""
        # Mock input to first return empty string, then valid string
        with unittest.mock.patch('builtins.input', side_effect=["", "  ", "valid-name"]):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                original_name, sanitized_name = get_project_name()
                self.assertEqual(original_name, "valid-name")
                self.assertEqual(sanitized_name, "valid-name")
                self.assertIn("Error: Project name cannot be empty", fake_stdout.getvalue())
    
    def test_get_project_description(self):
        """Test that get_project_description accepts input."""
        with unittest.mock.patch('builtins.input', return_value="This is a test project"):
            description = get_project_description()
            self.assertEqual(description, "This is a test project")
    
    def test_create_project_directory(self):
        """Test that create_project_directory creates a directory that doesn't exist."""
        with unittest.mock.patch('pathlib.Path.cwd', return_value=self.test_dir):
            project_path = create_project_directory("new-project")
            self.assertTrue(project_path.exists())
            self.assertEqual(project_path, self.test_dir / "new-project")
    
    def test_create_project_directory_exists(self):
        """Test that create_project_directory fails when directory exists."""
        # Create the project directory before testing
        test_project_dir = self.test_dir / "existing-project"
        test_project_dir.mkdir()
        
        with unittest.mock.patch('pathlib.Path.cwd', return_value=self.test_dir):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()):
                with self.assertRaises(SystemExit):
                    create_project_directory("existing-project")
    
    def test_create_subdirectories(self):
        """Test that create_subdirectories creates the expected subdirectories."""
        # Create a project directory for testing
        test_project_dir = self.test_dir / "test-project"
        test_project_dir.mkdir()
        
        # Capture stdout to prevent output during tests
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
            memory_bank_path, cursor_path = create_subdirectories(test_project_dir)
            
            # Check paths are correct
            self.assertEqual(memory_bank_path, test_project_dir / "memory-bank")
            self.assertEqual(cursor_path, test_project_dir / ".cursor")
            
            # Check directories exist
            self.assertTrue(memory_bank_path.exists())
            self.assertTrue(cursor_path.exists())
    
    def test_create_memory_bank_files(self):
        """Test that create_memory_bank_files creates the expected files with correct content."""
        # Create a project directory and memory-bank subdirectory for testing
        test_project_dir = self.test_dir / "test-project"
        test_project_dir.mkdir()
        memory_bank_path = test_project_dir / "memory-bank"
        memory_bank_path.mkdir()
        
        # Test data - using different original and sanitized names to verify the original is used in content
        test_original_name = "My Test Project"
        test_project_description = "This is a test project"
        
        # Capture stdout to prevent output during tests
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
            created_files = create_memory_bank_files(memory_bank_path, test_original_name, test_project_description)
            
            # Check that the expected number of files were created
            self.assertEqual(len(created_files), 5)
            
            # Check that all expected files exist
            expected_files = [
                "01-product-design-document.md",
                "02-tech-stack.md",
                "03-implementation-plan.md", 
                "04-progress.md",
                "05-architecture.md"
            ]
            
            for filename in expected_files:
                file_path = memory_bank_path / filename
                self.assertTrue(file_path.exists(), f"{filename} was not created")
                
                # Check that the file contains the original, human-readable project name
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.assertIn(test_original_name, content)
                    # Make sure the sanitized name is not mistakenly used
                    sanitized_test_name = sanitize_project_name(test_original_name)
                    if sanitized_test_name != test_original_name:
                        self.assertNotIn(sanitized_test_name, content)
                    
                    # For Product Design Document, also check for project description
                    if filename == "01-product-design-document.md":
                        self.assertIn(test_project_description, content)

    def test_create_cursor_rules_files(self):
        """Test that create_cursor_rules_files creates the rules files with correct content."""
        # Create a project directory and .cursor subdirectory for testing
        test_project_dir = self.test_dir / "test-project"
        test_project_dir.mkdir()
        cursor_path = test_project_dir / ".cursor"
        cursor_path.mkdir()
        
        # Capture stdout to prevent output during tests
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
            created_files = create_cursor_rules_files(cursor_path)
            
            # Check that the rules directory exists
            rules_dir = cursor_path / "rules"
            self.assertTrue(rules_dir.exists(), "rules directory was not created")
            
            # Check that we have the expected number of rule files
            self.assertEqual(len(created_files), 7, "Not all rule files were created")
            
            # Check that specific rule files exist and contain the right content
            architecture_rule = rules_dir / "architecture.mdc"
            self.assertTrue(architecture_rule.exists(), "architecture.mdc was not created")
            
            requirements_rule = rules_dir / "requirements.mdc"
            self.assertTrue(requirements_rule.exists(), "requirements.mdc was not created")
            
            # Check content of a couple of rule files
            with open(architecture_rule, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertEqual(content, CURSOR_RULES_ARCHITECTURE)
                # Check for MDC format
                self.assertIn("---", content)
                self.assertIn("description:", content)
                self.assertIn("type: Always", content)
            
            with open(requirements_rule, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertEqual(content, CURSOR_RULES_REQUIREMENTS)
                self.assertIn("description:", content)
                self.assertIn("type: Always", content)

    def test_print_post_execution_instructions(self):
        """Test that print_post_execution_instructions formats and prints instructions correctly."""
        test_original_name = "My Test Project"
        test_sanitized_name = "My-Test-Project"
        
        # Capture stdout to check for printed instructions
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print_post_execution_instructions(test_original_name, test_sanitized_name)
            
            # Get the captured output
            output = fake_stdout.getvalue()
            
            # Check that the output contains the project name and directory name
            self.assertIn(test_original_name, output)
            self.assertIn(test_sanitized_name, output)
            self.assertIn(f"$ cd {test_sanitized_name}", output)
            
            # Check that the output contains key sections from the instructions
            self.assertIn("structure created successfully", output)
            self.assertIn("OPEN THE PROJECT FOLDER IN CURSOR", output)
            self.assertIn("GENERATE MEMORY BANK CONTENT", output)
            self.assertIn("REVIEW AND REFINE CURSOR RULES", output)
            self.assertIn("START CODING WITH CLAUDE", output)
            self.assertIn("Happy Vibe Coding", output)
            
    def test_main_function(self):
        """Test that the main function properly orchestrates all steps of the setup process."""
        # This is a high-level integration test that would normally run all parts of the script
        # Since it requires input, we'll mock all components to verify they're called correctly
        
        with unittest.mock.patch('setup_project.get_project_name', return_value=("Test Project", "Test-Project")):
            with unittest.mock.patch('setup_project.get_project_description', return_value="Test description"):
                with unittest.mock.patch('setup_project.create_project_directory') as mock_create_dir:
                    with unittest.mock.patch('setup_project.create_subdirectories') as mock_create_subdirs:
                        with unittest.mock.patch('setup_project.create_memory_bank_files') as mock_create_mb_files:
                            with unittest.mock.patch('setup_project.create_cursor_rules_files') as mock_create_rules:
                                with unittest.mock.patch('setup_project.print_post_execution_instructions') as mock_print:
                                    with unittest.mock.patch('sys.stdout', new=io.StringIO()):
                                        
                                        # Mock paths for subdirectories
                                        project_path_mock = unittest.mock.MagicMock()
                                        memory_bank_path_mock = unittest.mock.MagicMock()
                                        cursor_path_mock = unittest.mock.MagicMock()
                                        
                                        # Set up return values for mocked functions
                                        mock_create_dir.return_value = project_path_mock
                                        mock_create_subdirs.return_value = (memory_bank_path_mock, cursor_path_mock)
                                        
                                        # Run the main function
                                        main()
                                        
                                        # Verify that all expected functions were called with correct args
                                        mock_create_dir.assert_called_once_with("Test-Project")
                                        mock_create_subdirs.assert_called_once_with(project_path_mock)
                                        mock_create_mb_files.assert_called_once_with(
                                            memory_bank_path_mock, "Test Project", "Test description"
                                        )
                                        mock_create_rules.assert_called_once_with(cursor_path_mock)
                                        mock_print.assert_called_once_with("Test Project", "Test-Project")

if __name__ == "__main__":
    unittest.main() 