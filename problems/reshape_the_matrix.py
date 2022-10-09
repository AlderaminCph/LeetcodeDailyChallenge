"""
In MATLAB, there is a handy function called reshape which can reshape an m x n
matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the
number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original
matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output
the new reshaped matrix; Otherwise, output the original matrix.



Example 1:

>>> Solution().matrixReshape([[1,2],[3,4]], 1, 4)
[[1, 2, 3, 4]]

Example 2:

>>> Solution().matrixReshape([[1,2],[3,4]], 2, 4)
[[1, 2], [3, 4]]
"""
from typing import List
import doctest


class Solution:
    def matrixReshape(
        self, mat: List[List[int]], r: int, c: int
    ) -> List[List[int]]:
        rows_num = len(mat)
        cols_num = len(mat[0])
        if r * c != rows_num * cols_num:  # reshape operation isn't possible
            return mat
        elements = []
        for row in range(rows_num):
            elements.extend(mat[row])
        elements = elements[::-1]
        reshaped_mat = []
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(elements.pop())
            reshaped_mat.append(new_row)
        return reshaped_mat


doctest.testmod()
