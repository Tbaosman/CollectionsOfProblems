#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def anagram_checker(s1: str, s2: str) -> bool:
    """
    Function to check if two strings are anagrams of each other.

    Parameters:
    s1 (str): The first input string.
    s2 (str): The second input string.

    Returns:
    bool: True if the strings are anagrams, False otherwise.

    Raises:
        assertionError: If the inputs are not strings.


    Examples:
    >>> anagram_checker("listen", "silent")
    True
    >>> anagram_checker("hello", "world")
    False
    >>> anagram_checker("rail safety", "fairy tales")
    True
    """
    assert isinstance(s1, str), "Input must be a string"
    assert isinstance(s2, str), "Input must be a string"

    is_anagram = sorted(s1.replace(" ", "").lower()) == sorted(
        s2.replace(" ", "").lower()
    )
    return is_anagram
