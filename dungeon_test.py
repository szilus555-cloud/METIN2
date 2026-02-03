#!/usr/bin/env python3
"""
Metin2 Automated Dungeon Testing Script
========================================

This script is designed for testing server security by automating dungeon traversal
in Metin2 using image recognition and automated interactions.

WARNING: This script is intended ONLY for testing on your own server in controlled 
conditions. Using automation tools may violate the game's terms of service.

Requirements:
- OpenCV (cv2) for image recognition
- PyAutoGUI for automated input
- PIL/Pillow for image processing
- numpy for array operations
"""

import time
import logging
import sys
from pathlib import Path
from typing import Optional, Tuple, List

try:
    import cv2
    import numpy as np
    import pyautogui
    from PIL import ImageGrab
except ImportError as e:
    print(f"Missing required library: {e}")
    print("Please install requirements: pip install -r requirements.txt")
    sys.exit(1)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dungeon_test.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DungeonAutomation:
    """Main class for automated dungeon testing in Metin2."""
    
    def __init__(self, config: dict):
        """
        Initialize the dungeon automation system.
        
        Args:
            config: Configuration dictionary with settings
        """
        self.config = config
        self.images_path = Path(config.get('images_path', 'images'))
        self.confidence = config.get('confidence', 0.8)
        self.delay = config.get('delay', 0.5)
        self.max_attempts = config.get('max_attempts', 3)
        self.dungeon_completed = False
        self.security_issues = []
        
        # Ensure images directory exists
        self.images_path.mkdir(exist_ok=True)
        
        # Safety: Enable PyAutoGUI fail-safe
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = self.delay
        
        logger.info("DungeonAutomation initialized")
        logger.warning("FAIL-SAFE: Move mouse to corner to abort")
    
    def find_image_on_screen(
        self, 
        template_name: str, 
        confidence: Optional[float] = None
    ) -> Optional[Tuple[int, int]]:
        """
        Find an image template on the screen using OpenCV.
        
        Args:
            template_name: Name of the template image file
            confidence: Confidence threshold (default: self.confidence)
            
        Returns:
            Tuple of (x, y) coordinates if found, None otherwise
        """
        if confidence is None:
            confidence = self.confidence
            
        template_path = self.images_path / template_name
        
        if not template_path.exists():
            logger.warning(f"Template image not found: {template_path}")
            return None
        
        try:
            # Capture current screen
            screenshot = ImageGrab.grab()
            screen_np = np.array(screenshot)
            screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
            
            # Load template
            template = cv2.imread(str(template_path))
            if template is None:
                logger.error(f"Failed to load template: {template_path}")
                return None
            
            # Perform template matching
            result = cv2.matchTemplate(screen_bgr, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= confidence:
                # Calculate center of matched region
                h, w = template.shape[:2]
                center_x = max_loc[0] + w // 2
                center_y = max_loc[1] + h // 2
                logger.info(f"Found '{template_name}' at ({center_x}, {center_y}) "
                          f"with confidence {max_val:.2f}")
                return (center_x, center_y)
            else:
                logger.debug(f"'{template_name}' not found (max confidence: {max_val:.2f})")
                return None
                
        except Exception as e:
            logger.error(f"Error during image recognition: {e}")
            return None
    
    def click_at_position(self, x: int, y: int, clicks: int = 1):
        """
        Click at specified screen position.
        
        Args:
            x: X coordinate
            y: Y coordinate
            clicks: Number of clicks (default: 1)
        """
        try:
            pyautogui.click(x, y, clicks=clicks)
            logger.info(f"Clicked at ({x}, {y})")
            time.sleep(self.delay)
        except Exception as e:
            logger.error(f"Error clicking at ({x}, {y}): {e}")
    
    def click_image(self, template_name: str, clicks: int = 1) -> bool:
        """
        Find and click on an image template.
        
        Args:
            template_name: Name of the template image file
            clicks: Number of clicks (default: 1)
            
        Returns:
            True if image was found and clicked, False otherwise
        """
        position = self.find_image_on_screen(template_name)
        if position:
            self.click_at_position(*position, clicks=clicks)
            return True
        return False
    
    def press_key(self, key: str, presses: int = 1):
        """
        Simulate pressing a keyboard key.
        
        Args:
            key: Key to press (e.g., 'space', 'w', 'a', 's', 'd', '1', '2')
            presses: Number of times to press (default: 1)
        """
        try:
            for _ in range(presses):
                pyautogui.press(key)
                time.sleep(0.1)
            logger.info(f"Pressed key '{key}' {presses} time(s)")
        except Exception as e:
            logger.error(f"Error pressing key '{key}': {e}")
    
    def enter_dungeon(self) -> bool:
        """
        Attempt to enter the dungeon by finding and clicking the entrance.
        
        Returns:
            True if entrance was found and clicked, False otherwise
        """
        logger.info("Attempting to enter dungeon...")
        
        for attempt in range(self.max_attempts):
            logger.info(f"Entrance attempt {attempt + 1}/{self.max_attempts}")
            
            # Look for dungeon entrance NPC
            if self.click_image('dungeon_npc.png'):
                time.sleep(1)
                
                # Look for enter button
                if self.click_image('enter_button.png'):
                    logger.info("Successfully entered dungeon")
                    time.sleep(2)
                    return True
            
            time.sleep(1)
        
        logger.warning("Failed to enter dungeon after maximum attempts")
        self.security_issues.append("Unable to locate dungeon entrance - detection may be inadequate")
        return False
    
    def move_character(self, direction: str, duration: float = 1.0):
        """
        Move character in specified direction.
        
        Args:
            direction: Direction to move ('forward', 'back', 'left', 'right')
            duration: How long to hold the key (seconds)
        """
        key_map = {
            'forward': 'w',
            'back': 's',
            'left': 'a',
            'right': 'd'
        }
        
        key = key_map.get(direction.lower())
        if not key:
            logger.error(f"Invalid direction: {direction}")
            return
        
        try:
            pyautogui.keyDown(key)
            time.sleep(duration)
            pyautogui.keyUp(key)
            logger.info(f"Moved {direction} for {duration}s")
        except Exception as e:
            logger.error(f"Error moving character: {e}")
    
    def attack_enemies(self, skill_keys: List[str] = ['1', '2', '3']) -> bool:
        """
        Attack enemies using configured skill keys.
        
        Args:
            skill_keys: List of keys for skills (default: ['1', '2', '3'])
            
        Returns:
            True if enemies were detected, False otherwise
        """
        logger.info("Searching for enemies...")
        
        # Look for enemy indicator
        enemy_pos = self.find_image_on_screen('enemy_indicator.png', confidence=0.7)
        
        if enemy_pos:
            logger.info("Enemy detected! Starting combat...")
            
            # Click on enemy to target
            self.click_at_position(*enemy_pos)
            time.sleep(0.5)
            
            # Use skills in rotation
            for _ in range(3):  # Attack 3 times
                for key in skill_keys:
                    self.press_key(key)
                    time.sleep(0.3)
            
            logger.info("Combat sequence completed")
            return True
        else:
            logger.debug("No enemies detected")
            return False
    
    def check_dungeon_completion(self) -> bool:
        """
        Check if dungeon has been completed.
        
        Returns:
            True if completion indicator found, False otherwise
        """
        logger.info("Checking for dungeon completion...")
        
        # Look for completion notification or exit portal
        if self.find_image_on_screen('dungeon_complete.png', confidence=0.75):
            logger.info("Dungeon completion detected!")
            self.dungeon_completed = True
            return True
        
        return False
    
    def navigate_dungeon(self, max_duration: int = 300):
        """
        Main navigation logic for traversing the dungeon.
        
        Args:
            max_duration: Maximum time to spend in dungeon (seconds)
        """
        logger.info("Starting dungeon navigation...")
        start_time = time.time()
        
        while time.time() - start_time < max_duration:
            # Check for completion
            if self.check_dungeon_completion():
                break
            
            # Look for and attack enemies
            if self.attack_enemies():
                time.sleep(2)
                continue
            
            # Move forward if no enemies
            self.move_character('forward', duration=2)
            time.sleep(1)
            
            # Occasionally check sides
            if int(time.time() - start_time) % 10 == 0:
                self.move_character('right', duration=1)
                time.sleep(0.5)
        
        if not self.dungeon_completed:
            logger.warning("Dungeon not completed within time limit")
            self.security_issues.append("Timeout: Automation unable to complete dungeon efficiently")
    
    def run_test(self) -> dict:
        """
        Execute complete dungeon test sequence.
        
        Returns:
            Dictionary with test results
        """
        logger.info("=" * 60)
        logger.info("Starting Metin2 Dungeon Automation Test")
        logger.info("=" * 60)
        
        start_time = time.time()
        
        try:
            # Step 1: Enter dungeon
            if not self.enter_dungeon():
                return self._generate_report(start_time, success=False)
            
            # Step 2: Navigate and clear dungeon
            self.navigate_dungeon(max_duration=self.config.get('max_dungeon_time', 300))
            
            # Step 3: Exit (if completed)
            if self.dungeon_completed:
                logger.info("Attempting to exit dungeon...")
                self.click_image('exit_portal.png')
                time.sleep(2)
            
            return self._generate_report(start_time, success=self.dungeon_completed)
            
        except KeyboardInterrupt:
            logger.warning("Test interrupted by user")
            return self._generate_report(start_time, success=False, interrupted=True)
        except Exception as e:
            logger.error(f"Unexpected error during test: {e}", exc_info=True)
            return self._generate_report(start_time, success=False, error=str(e))
    
    def _generate_report(
        self, 
        start_time: float, 
        success: bool, 
        interrupted: bool = False,
        error: Optional[str] = None
    ) -> dict:
        """
        Generate test report.
        
        Args:
            start_time: Test start timestamp
            success: Whether test was successful
            interrupted: Whether test was interrupted
            error: Error message if any
            
        Returns:
            Dictionary with test results
        """
        duration = time.time() - start_time
        
        report = {
            'success': success,
            'duration': duration,
            'dungeon_completed': self.dungeon_completed,
            'security_issues': self.security_issues,
            'interrupted': interrupted,
            'error': error
        }
        
        logger.info("=" * 60)
        logger.info("Test Report")
        logger.info("=" * 60)
        logger.info(f"Test Duration: {duration:.2f} seconds")
        logger.info(f"Dungeon Completed: {self.dungeon_completed}")
        
        if self.security_issues:
            logger.warning("Security Issues Detected:")
            for issue in self.security_issues:
                logger.warning(f"  - {issue}")
        else:
            logger.info("No security issues detected")
        
        if interrupted:
            logger.warning("Test was interrupted")
        
        if error:
            logger.error(f"Error occurred: {error}")
        
        logger.info("=" * 60)
        
        return report


def load_config() -> dict:
    """
    Load configuration from file or use defaults.
    
    Returns:
        Configuration dictionary
    """
    # Default configuration
    config = {
        'images_path': 'images',
        'confidence': 0.8,
        'delay': 0.5,
        'max_attempts': 3,
        'max_dungeon_time': 300,
        'skill_keys': ['1', '2', '3']
    }
    
    # Try to load from config file if it exists
    config_file = Path('config.json')
    if config_file.exists():
        try:
            import json
            with open(config_file, 'r') as f:
                loaded_config = json.load(f)
                config.update(loaded_config)
                logger.info(f"Loaded configuration from {config_file}")
        except Exception as e:
            logger.warning(f"Failed to load config file: {e}, using defaults")
    
    return config


def main():
    """Main entry point for the script."""
    print("=" * 60)
    print("Metin2 Automated Dungeon Testing Script")
    print("=" * 60)
    print()
    print("WARNING: This script is for testing purposes only!")
    print("Use only on your own server in controlled conditions.")
    print()
    print("Press Ctrl+C to abort at any time.")
    print("Move mouse to screen corner to trigger fail-safe.")
    print()
    
    # Give user time to read warning
    for i in range(5, 0, -1):
        print(f"Starting in {i}...", end='\r')
        time.sleep(1)
    print()
    
    # Load configuration
    config = load_config()
    
    # Initialize automation
    automation = DungeonAutomation(config)
    
    # Run test
    result = automation.run_test()
    
    # Exit with appropriate code
    sys.exit(0 if result['success'] else 1)


if __name__ == '__main__':
    main()
