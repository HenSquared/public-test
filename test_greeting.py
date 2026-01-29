#!/usr/bin/env python3
"""
Unit tests for the greeting utility module.
"""

import unittest
from greeting import greet, greet_multiple


class TestGreeting(unittest.TestCase):
    """Test cases for greeting functions."""
    
    def test_greet_basic(self):
        """Test basic greeting functionality."""
        result = greet("World")
        self.assertEqual(result, "Hello, World! Welcome to the agent task implementation.")
    
    def test_greet_with_different_names(self):
        """Test greeting with various names."""
        self.assertIn("Alice", greet("Alice"))
        self.assertIn("Bob", greet("Bob"))
    
    def test_greet_empty_string(self):
        """Test that empty string raises ValueError."""
        with self.assertRaises(ValueError):
            greet("")
    
    def test_greet_none(self):
        """Test that None raises ValueError."""
        with self.assertRaises(ValueError):
            greet(None)
    
    def test_greet_invalid_type(self):
        """Test that invalid types raise ValueError."""
        with self.assertRaises(ValueError):
            greet(123)
    
    def test_greet_multiple_basic(self):
        """Test greeting multiple people."""
        names = ["Alice", "Bob", "Charlie"]
        results = greet_multiple(names)
        self.assertEqual(len(results), 3)
        self.assertIn("Alice", results[0])
        self.assertIn("Bob", results[1])
        self.assertIn("Charlie", results[2])
    
    def test_greet_multiple_empty_list(self):
        """Test greeting with empty list."""
        results = greet_multiple([])
        self.assertEqual(results, [])
    
    def test_greet_multiple_invalid_type(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError):
            greet_multiple("not a list")


if __name__ == "__main__":
    unittest.main()
