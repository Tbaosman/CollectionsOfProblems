#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""   
Test module for missing_number function.
Contains correct tests to help identify bugs in the implementation. 

Test categories:
    - Standard cases: typical list inputs
    - Edge cases: empty lists, equal lists
    - Defensive tests: invalid inputs
        
Created on 2024-12-25
Author: Mohamed Saeed
"""
import unittest
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Solutions.missing_number import missing_number

class TestMissingNumber(unittest.TestCase):
    """
    Test class for the missing_number function.
    """

    def test_standard_cases(self):
        """
        Test the function with standard inputs.
        """
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_edge_cases(self):
        """
        Test the function with edge inputs.
        """
        with self.assertRaises(ValueError):
            missing_number([])

    def test_defensive_cases(self):
        """
        Test the function with invalid inputs.
        """
        with self.assertRaises(AssertionError):
            missing_number(123)
            
if __name__ == "__main__":
    unittest.main()