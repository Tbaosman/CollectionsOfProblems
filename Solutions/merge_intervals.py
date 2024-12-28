#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge_intervals(intervals: list) -> list:
    """
    Function to merge overlapping intervals.

    Parameters:
    intervals (list): A list of intervals to merge.

    Returns:
    list: The merged intervals.
    
    Raises:
        AssertionError: If the input is not a list.
        

    Examples:
    >>> merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge_intervals([[1, 4], [4, 5]])
    [[1, 5]]
    >>> merge_intervals([[1, 4], [0, 4]])
    [[0, 4]]
    """
    if not intervals:
        return []
    assert isinstance(intervals, list), "Input must be a list."

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged