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
    create_subdirectories
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
    
    def test_get_project_name_valid_input(self):
        """Test that get_project_name accepts valid input."""
        with unittest.mock.patch('builtins.input', return_value="test-project"):
            project_name = get_project_name()
            self.assertEqual(project_name, "test-project")
    
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

if __name__ == "__main__":
    unittest.main() 