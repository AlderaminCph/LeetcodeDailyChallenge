"""
Given an integer array nums, return true if any value appears at least twice in
 the array, and return false if every element is distinct.



Example 1:

>>> Solution().containsDuplicate([1,2,3,1])
True

Example 2:

>>> Solution().containsDuplicate([1,2,3,4])
False

Example 3:

>>> Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
True
"""
from typing import List
import doctest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


doctest.testmod()
