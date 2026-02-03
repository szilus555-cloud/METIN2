#!/usr/bin/env python3
"""
Unit tests for dungeon_test.py

These tests verify the basic structure and functionality without requiring
the full dependency stack (OpenCV, PyAutoGUI, etc.)
"""

import unittest
import sys
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path


class TestDungeonAutomationStructure(unittest.TestCase):
    """Test the structure of the DungeonAutomation class."""
    
    @patch('dungeon_test.cv2')
    @patch('dungeon_test.pyautogui')
    @patch('dungeon_test.ImageGrab')
    def setUp(self, mock_imagegrab, mock_pyautogui, mock_cv2):
        """Set up test fixtures."""
        # Mock the dependencies
        self.mock_cv2 = mock_cv2
        self.mock_pyautogui = mock_pyautogui
        self.mock_imagegrab = mock_imagegrab
        
        # Import after mocking
        from dungeon_test import DungeonAutomation
        
        self.DungeonAutomation = DungeonAutomation
        
        # Test configuration
        self.config = {
            'images_path': 'test_images',
            'confidence': 0.8,
            'delay': 0.1,
            'max_attempts': 2,
            'max_dungeon_time': 10
        }
    
    @patch('dungeon_test.cv2')
    @patch('dungeon_test.pyautogui')
    @patch('dungeon_test.ImageGrab')
    def test_initialization(self, mock_imagegrab, mock_pyautogui, mock_cv2):
        """Test that DungeonAutomation initializes correctly."""
        from dungeon_test import DungeonAutomation
        
        automation = DungeonAutomation(self.config)
        
        self.assertEqual(automation.config, self.config)
        self.assertEqual(automation.confidence, 0.8)
        self.assertEqual(automation.delay, 0.1)
        self.assertEqual(automation.max_attempts, 2)
        self.assertFalse(automation.dungeon_completed)
        self.assertEqual(automation.security_issues, [])
    
    @patch('dungeon_test.cv2')
    @patch('dungeon_test.pyautogui')
    @patch('dungeon_test.ImageGrab')
    def test_config_defaults(self, mock_imagegrab, mock_pyautogui, mock_cv2):
        """Test that default configuration values are set."""
        from dungeon_test import load_config
        
        config = load_config()
        
        self.assertIn('images_path', config)
        self.assertIn('confidence', config)
        self.assertIn('delay', config)
        self.assertIn('max_attempts', config)
        self.assertIn('max_dungeon_time', config)
    
    @patch('dungeon_test.cv2')
    @patch('dungeon_test.pyautogui')
    @patch('dungeon_test.ImageGrab')
    def test_methods_exist(self, mock_imagegrab, mock_pyautogui, mock_cv2):
        """Test that all required methods exist."""
        from dungeon_test import DungeonAutomation
        
        automation = DungeonAutomation(self.config)
        
        # Check that all main methods exist
        self.assertTrue(hasattr(automation, 'find_image_on_screen'))
        self.assertTrue(hasattr(automation, 'click_at_position'))
        self.assertTrue(hasattr(automation, 'click_image'))
        self.assertTrue(hasattr(automation, 'press_key'))
        self.assertTrue(hasattr(automation, 'enter_dungeon'))
        self.assertTrue(hasattr(automation, 'move_character'))
        self.assertTrue(hasattr(automation, 'attack_enemies'))
        self.assertTrue(hasattr(automation, 'check_dungeon_completion'))
        self.assertTrue(hasattr(automation, 'navigate_dungeon'))
        self.assertTrue(hasattr(automation, 'run_test'))
        self.assertTrue(hasattr(automation, '_generate_report'))
    
    @patch('dungeon_test.cv2')
    @patch('dungeon_test.pyautogui')
    @patch('dungeon_test.ImageGrab')
    def test_generate_report(self, mock_imagegrab, mock_pyautogui, mock_cv2):
        """Test report generation."""
        from dungeon_test import DungeonAutomation
        import time
        
        automation = DungeonAutomation(self.config)
        automation.dungeon_completed = True
        automation.security_issues = ['Test issue']
        
        start_time = time.time()
        report = automation._generate_report(start_time, success=True)
        
        self.assertIn('success', report)
        self.assertIn('duration', report)
        self.assertIn('dungeon_completed', report)
        self.assertIn('security_issues', report)
        self.assertTrue(report['success'])
        self.assertTrue(report['dungeon_completed'])
        self.assertEqual(len(report['security_issues']), 1)


class TestConfigurationFile(unittest.TestCase):
    """Test configuration file handling."""
    
    def test_config_json_exists(self):
        """Test that config.json file exists."""
        config_path = Path('config.json')
        self.assertTrue(config_path.exists(), "config.json should exist")
    
    def test_config_json_valid(self):
        """Test that config.json is valid JSON."""
        import json
        
        config_path = Path('config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Check required fields
        self.assertIn('images_path', config)
        self.assertIn('confidence', config)
        self.assertIn('delay', config)
        self.assertIn('max_attempts', config)


class TestRequirements(unittest.TestCase):
    """Test requirements file."""
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists."""
        req_path = Path('requirements.txt')
        self.assertTrue(req_path.exists(), "requirements.txt should exist")
    
    def test_requirements_contains_dependencies(self):
        """Test that requirements.txt contains necessary packages."""
        req_path = Path('requirements.txt')
        with open(req_path, 'r') as f:
            content = f.read()
        
        self.assertIn('opencv', content.lower())
        self.assertIn('numpy', content.lower())
        self.assertIn('pillow', content.lower())
        self.assertIn('pyautogui', content.lower())


class TestDocumentation(unittest.TestCase):
    """Test documentation files."""
    
    def test_readme_exists(self):
        """Test that README.md exists."""
        readme_path = Path('README.md')
        self.assertTrue(readme_path.exists(), "README.md should exist")
    
    def test_readme_contains_warnings(self):
        """Test that README contains appropriate warnings."""
        readme_path = Path('README.md')
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for warning section
        self.assertIn('WARNING', content.upper())
        self.assertIn('OSTRZEŻENIE', content.upper())
    
    def test_images_readme_exists(self):
        """Test that images/README.md exists."""
        images_readme = Path('images/README.md')
        self.assertTrue(images_readme.exists(), "images/README.md should exist")


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
