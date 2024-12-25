#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for long_substring function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical string inputs
    - Edge cases: empty strings, equal 
    - Defensive tests: invalid inputs

Created on 2024-12-25
Author: Mohamed Saeed
"""

import unittest
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Solutions.longest_substring import longest_substring

class TestFindLongest(unittest.TestCase):
    """
    Test class for the longest_substring function.
    """

    def test_standard_cases(self):
        """
        Test the function with standard inputs.
        """
        self.assertEqual(longest_substring("abcabcbb"), "abc")

    def test_edge_cases(self):
        """
        Test the function with edge inputs.
        """
        with self.assertRaises(ValueError):
            longest_substring("")

    def test_defensive_cases(self):
        """
        Test the function with invalid inputs.
        """
        with self.assertRaises(AssertionError):
            longest_substring(123)

if __name__ == "__main__":
    unittest.main()