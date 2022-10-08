"""
Given an integer array nums of length n and an integer target, find three
integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.


Example 1:

>>> Solution().threeSumClosest([-1,2,1,-4], 1)
2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

>>> Solution().threeSumClosest([0,0,0], 1)
0

Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""
from typing import List
import doctest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 100000
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                if summ == target:
                    return summ
                if abs(summ - target) < abs(res - target):
                    res = summ
                if summ <= target:
                    start += 1
                    while (nums[start] == nums[start-1] and start < end):
                        start += 1
                else:
                    end -= 1
        return res


doctest.testmod()
