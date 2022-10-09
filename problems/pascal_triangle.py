"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above
it as shown:



Example 1:

>>> Solution().generate(5)
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

>>> Solution().generate(1)
[[1]]
"""
from typing import List
import doctest


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            res = [[1]]
        elif numRows == 1:
            res = [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            for i in range(2, numRows):
                row = [1]
                for j in range(len(res[i - 1]) - 1):
                    row.append(sum(res[i - 1][j], res[i - 1][j + 1]))
                row.append(1)
                res.append(row)
        return res


doctest.testmod()
