#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test module for anagram_checker function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical string inputs
    - Edge cases: empty strings, equal strings
    - Defensive tests: invalid inputs

created on 2024-12-28
author: Mohamed Saeed
"""

import unittest
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Solutions.anagram_checker import anagram_checker


class TestAnagramChecker(unittest.TestCase):
    """
    Test class for the anagram_checker function.
    """

    def test_standard_cases(self):
        """
        Test the function with standard inputs.
        """
        self.assertTrue(anagram_checker("listen", "silent"))

    def test_edge_cases(self):
        """
        Test the function with edge inputs.
        """
        self.assertFalse(anagram_checker("hello", "world"))

    def test_empty_strings(self):
        """
        Test the function with empty strings.
        """
        self.assertTrue(anagram_checker("", ""))

    def test_equal_strings(self):
        """
        Test the function with equal strings.
        """
        self.assertTrue(anagram_checker("hello", "hello"))

    def test_case_insensitive(self):
        """
        Test the function with case-insensitive strings.
        """
        self.assertTrue(anagram_checker("Rail safety", "Fairy tales"))

    def test_defensive_cases(self):
        """
        Test the function with invalid inputs.
        """
        with self.assertRaises(AssertionError):
            anagram_checker(123, 456)
            
if __name__ == "__main__":
    unittest.main()
