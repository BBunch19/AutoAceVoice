#!/usr/bin/env python3

import unittest
from src.command_processor import CommandProcessor

class TestCommandProcessor(unittest.TestCase):
    """Tests for the CommandProcessor class"""
    
    def setUp(self):
        self.processor = CommandProcessor()
    
    def test_basic_commands(self):
        """Test basic command processing"""
        # Test open command
        result = self.processor.process_command("open browser")
        self.assertEqual(result, "Opening browser")
        
        # Test search command
        result = self.processor.process_command("search for python tutorials")
        self.assertEqual(result, "Searching for for python tutorials")
        
        # Test help command
        result = self.processor.process_command("help")
        self.assertTrue(result.startswith("Available commands:"))
    
    def test_unknown_command(self):
        """Test handling of unknown commands"""
        result = self.processor.process_command("unknowncommand test")
        self.assertEqual(result, "Unknown command: unknowncommand")
    
    def test_empty_command(self):
        """Test handling of empty commands"""
        result = self.processor.process_command("")
        self.assertEqual(result, "No command received")
    
    def test_register_command(self):
        """Test registering a new command"""
        def custom_handler(args):
            return f"Custom command executed with args: {' '.join(args)}"
        
        self.processor.register_command("custom", custom_handler)
        result = self.processor.process_command("custom arg1 arg2")
        self.assertEqual(result, "Custom command executed with args: arg1 arg2")

if __name__ == "__main__":
    unittest.main()
