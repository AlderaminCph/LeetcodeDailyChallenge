"""
Given an integer array nums of length n and an integer target, find three
integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.


Example 1:

>>> Solution().treeSumClosest([-1,2,1,-4], 1)
2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

>>> Solution().treeSumClosest([0,0,0], 1)
0

Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""
from typing import List
import doctest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            summ = sum(nums[i], nums[start], nums[end])
            if res < summ:
                res = summ
            while start < end:
                if summ < target:
                    start += 1
                if summ > target:
                    end -= 1
        return res


doctest.testmod()
