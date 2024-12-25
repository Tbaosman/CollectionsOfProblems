#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def missing_number(nums: list) -> int:
    """
    Function to find the missing number in a list of numbers from 0 to n.
    
    Parameters:
    nums (list): The input list of numbers.
    
    Returns:
    int: The missing number.
    
    Raises:
        assertionError: If the input is not a list
        ValueError: If the input list is empty.
        
    Examples:
    >>> missing_number([3, 0, 1])
    2
    >>> missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
    8
    >>> missing_number([0])
    1
    """
    assert isinstance(nums, list), "Input must be a list"
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)