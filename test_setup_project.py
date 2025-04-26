#!/usr/bin/env python3

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
    create_memory_bank_files
)

class TestSetupProject(unittest.TestCase):
    
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
                project_name = get_project_name()
                self.assertEqual(project_name, "test-project")
                self.assertIn("Project name sanitized to", fake_stdout.getvalue())
    
    def test_get_project_name_already_sanitized(self):
        """Test that get_project_name accepts already sanitized input."""
        with unittest.mock.patch('builtins.input', return_value="test-project"):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                project_name = get_project_name()
                self.assertEqual(project_name, "test-project")
                self.assertNotIn("Project name sanitized to", fake_stdout.getvalue())
    
    def test_get_project_name_empty_then_valid(self):
        """Test that get_project_name rejects empty input then accepts valid input."""
        # Mock input to first return empty string, then valid string
        with unittest.mock.patch('builtins.input', side_effect=["", "  ", "valid-name"]):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                project_name = get_project_name()
                self.assertEqual(project_name, "valid-name")
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
        
        # Test data
        test_project_name = "test-project"
        test_project_description = "This is a test project"
        
        # Capture stdout to prevent output during tests
        with unittest.mock.patch('sys.stdout', new=io.StringIO()):
            created_files = create_memory_bank_files(memory_bank_path, test_project_name, test_project_description)
            
            # Check that the expected number of files were created
            self.assertEqual(len(created_files), 5)
            
            # Check that all expected files exist
            expected_files = [
                "product-requirements-document.md",
                "tech-stack.md",
                "implementation-plan.md",
                "progress.md",
                "architecture.md"
            ]
            
            for filename in expected_files:
                file_path = memory_bank_path / filename
                self.assertTrue(file_path.exists(), f"{filename} was not created")
                
                # Check that the file contains the project name
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.assertIn(test_project_name, content)
                    
                    # For PRD, also check for project description
                    if filename == "product-requirements-document.md":
                        self.assertIn(test_project_description, content)

if __name__ == "__main__":
    unittest.main() 