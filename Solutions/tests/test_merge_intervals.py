#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Test module for merge_intervals function.
    Contains correct tests to help identify bugs in the implementation.
    
    Test categories:
        - Standard cases: typical list inputs
        - Edge cases: empty lists, equal lists
        - Defensive tests: invalid inputs
        
    Created on 2024-12-28
    author: Mohamed Saeed
    
"""
import unittest
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from Solutions.merge_intervals import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    """
    Test class for the merge_intervals function.
    """

    def test_standard_cases(self):
        """
        Test the function with standard inputs.
        """
        self.assertEqual(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
                        [[1, 6], [8, 10], [15, 18]])
        
    def test_non_overlapping_intervals(self):
        """
        Test the function with non-overlapping intervals.
        """
        self.assertEqual(merge_intervals([[1, 4], [5, 9]]), [[1, 4], [5, 9]])
        
    def test_equal_intervals(self):
        """
        Test the function with equal intervals.
        """
        self.assertEqual(merge_intervals([[1, 4], [1, 4]]), [[1, 4]])

    def test_edge_cases(self):
        """
        Test the function with edge inputs.
        """
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])

    def test_empty_list(self):
        """
        Test the function with an empty list.
        """
        self.assertEqual(merge_intervals([]), [])

    def test_defensive_cases(self):
        """
        Test the function with invalid inputs.
        """
        with self.assertRaises(AssertionError):
            merge_intervals(123)
            
if __name__ == "__main__":
    unittest.main()