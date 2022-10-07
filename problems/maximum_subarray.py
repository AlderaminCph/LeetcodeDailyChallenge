"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

>>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
6

Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

>>> Solution().maxSubArray([1])
1

Example 3:

>>> Solution().maxSubArray([5,4,-1,7,8])
23
"""
from typing import List
import doctest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
        return maxSub


doctest.testmod()
