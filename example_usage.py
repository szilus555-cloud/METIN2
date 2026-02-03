#!/usr/bin/env python3
"""
Example usage of the Metin2 Dungeon Automation Script

This file demonstrates how to use the dungeon_test module programmatically
with custom configurations.
"""

import sys
from pathlib import Path

# Import the dungeon automation module
from dungeon_test import DungeonAutomation, logger


def example_basic_usage():
    """Basic usage example with default configuration."""
    print("Example 1: Basic usage with defaults")
    print("-" * 50)
    
    config = {
        'images_path': 'images',
        'confidence': 0.8,
        'delay': 0.5,
        'max_attempts': 3,
        'max_dungeon_time': 300
    }
    
    automation = DungeonAutomation(config)
    result = automation.run_test()
    
    print(f"\nTest completed: {result['success']}")
    print(f"Duration: {result['duration']:.2f}s")
    

def example_custom_config():
    """Example with custom configuration for faster testing."""
    print("\n\nExample 2: Custom configuration")
    print("-" * 50)
    
    config = {
        'images_path': 'images',
        'confidence': 0.75,  # Lower confidence for more matches
        'delay': 0.3,        # Faster actions
        'max_attempts': 5,   # More attempts to enter dungeon
        'max_dungeon_time': 180  # 3 minutes max
    }
    
    automation = DungeonAutomation(config)
    
    # You can also use individual methods
    logger.info("Testing image recognition...")
    
    # Test finding an image
    npc_pos = automation.find_image_on_screen('dungeon_npc.png')
    if npc_pos:
        print(f"Found NPC at position: {npc_pos}")
    else:
        print("NPC not found - make sure game is running and visible")


def example_manual_control():
    """Example of manual step-by-step control."""
    print("\n\nExample 3: Manual step-by-step control")
    print("-" * 50)
    
    config = {
        'images_path': 'images',
        'confidence': 0.8,
        'delay': 0.5,
        'max_attempts': 3,
        'max_dungeon_time': 300
    }
    
    automation = DungeonAutomation(config)
    
    # Manual steps
    print("Step 1: Attempting to enter dungeon...")
    if automation.enter_dungeon():
        print("✓ Successfully entered dungeon")
        
        print("\nStep 2: Looking for enemies...")
        if automation.attack_enemies(['1', '2', '3']):
            print("✓ Attacked enemies")
        
        print("\nStep 3: Moving character...")
        automation.move_character('forward', duration=2)
        print("✓ Moved forward")
        
        print("\nStep 4: Checking completion...")
        if automation.check_dungeon_completion():
            print("✓ Dungeon completed!")
    else:
        print("✗ Failed to enter dungeon")


def main():
    """Main function to run examples."""
    print("=" * 60)
    print("Metin2 Dungeon Automation - Usage Examples")
    print("=" * 60)
    print()
    print("Choose an example to run:")
    print("1. Basic usage with defaults")
    print("2. Custom configuration")
    print("3. Manual step-by-step control")
    print("0. Exit")
    print()
    
    try:
        choice = input("Enter choice (0-3): ").strip()
        
        if choice == '1':
            example_basic_usage()
        elif choice == '2':
            example_custom_config()
        elif choice == '3':
            example_manual_control()
        elif choice == '0':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice!")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
