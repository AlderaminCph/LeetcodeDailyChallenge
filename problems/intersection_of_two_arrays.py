"""
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as it shows
in both arrays and you may return the result in any order.



Example 1:

>>> Solution().intersect([1,2,2,1], [2,2])
[2, 2]

Example 2:

>>> Solution().intersect([4,9,5], [9,4,9,8,4])
[4, 9]

Explanation: [9,4] is also accepted.

>>> Solution().intersect([3,1,2], [1,1])
[1]
"""
from typing import List
from collections import defaultdict
import doctest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            little_arr = nums2
            big_arr = nums1
        else:
            little_arr = nums1
            big_arr = nums2
        hashtable = defaultdict(int)
        for i in little_arr:
            if i not in hashtable:
                hashtable[i] = 0
            if i in big_arr and hashtable[i] < big_arr.count(i):
                hashtable[i] += 1
        res = []
        for key, val in hashtable.items():
            if val >= 1:
                res += [key] * val

        return res


doctest.testmod()
