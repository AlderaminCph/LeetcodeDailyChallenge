"""
Given an integer array nums, return the largest perimeter of a triangle with
a non-zero area, formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

>>> largestPerimeter([2,1,2])
5

Example 2:

>>> largestPerimeter([1,2,1])
0

>>> largestPerimeter([1,2,2,4,18,8])
5

>>> largestPerimeter([3,2,3,4])
10
"""
from typing import List
import doctest


def largestPerimeter(nums: List[int]) -> int:
    nums.sort(reverse=True)

    while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
        nums.pop(0)

    return 0 if len(nums) < 3 else sum(nums[:3])


doctest.testmod()
