"""
Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous
row.



Example 1:

>>> searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
True

Example 2:

>>> searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
False
"""
from typing import List
import doctest


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # Solution Idea: double binary search

    rows, cols = len(matrix), len(matrix[0])  # matrix dimension

    # looking for the row we need to find:
    top_row, bottom_row = 0, rows - 1
    while top_row <= bottom_row:
        middle_row = (top_row + bottom_row) // 2
        if target > matrix[middle_row][-1]:  # most right value
            top_row = middle_row + 1
        elif target < matrix[middle_row][0]:
            bottom_row = middle_row - 1
        else:
            break

    if not (top_row <= bottom_row):
        return False

    # second binary search
    # run binary search on the current row
    middle_row = (top_row + bottom_row) // 2
    left, right = 0, cols - 1
    while left <= right:
        midlle = (left + right) // 2
        if target > matrix[middle_row][midlle]:
            left = midlle + 1
        elif target < matrix[middle_row][midlle]:
            right = midlle - 1
        else:
            return True
    return False


doctest.testmod()
