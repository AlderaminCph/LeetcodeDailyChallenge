"""
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as it shows
in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

"""
from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            little_arr = nums2
            big_arr = nums1
        else:
            little_arr = nums1
            big_arr = nums2
        hashtable = defaultdict(int)
        for i in range(len(little_arr)):
            hashtable[i] = 0
            if hashtable[i] in big_arr:
                hashtable[i] += 1
        res = list(hashtable.keys())[
            [i for i in list(hashtable.values()) if i >= 1]
        ]  # noqa
        return res
