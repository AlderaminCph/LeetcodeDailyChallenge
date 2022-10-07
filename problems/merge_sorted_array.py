"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of
m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length
of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
>>> Solution().merge([1,2,3,0,0,0], 3,[2,5,6],3)
[1, 2, 2, 3, 5, 6]

Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.

Example 2:

>>> Solution().merge([1],1,[],0)
[1]

Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

>>> Solution().merge([0],0,[1], 1)
[1]

Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to
 ensure the merge result can fit in nums1.

>>> Solution().merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)
[-1, 0, 0, 1, 2, 2, 3, 3, 3]

>>> Solution().merge([-50, -48, -47, -47, -46, -44, -43, -43, -41, -39, -38, -37, -37, -37, -33, -33, -32, -31, -29, -29, -27, -26, -26, -26, -25, -25, -24, -24, -23, -22, -22, -22, -18, -17, -17, -14, -14, -11, -11, -11, -6, -5, -5, -5, -5, -4, -1,0,2,2,2,2,5,6,7,7,9,10,13,13,14,14,18,21,21,21,22,24,24,24,25,26,26,29,29,29,30,30,31,31,32,33,34,34,34,35,38,40,41,42,43,44,44,46,46,47,47,48,49,49],100,[],0) # noqa
[-50, -48, -47, -47, -46, -44, -43, -43, -41, -39, -38, -37, -37, -37, -33, -33, -32, -31, -29, -29, -27, -26, -26, -26, -25, -25, -24, -24, -23, -22, -22, -22, -18, -17, -17, -14, -14, -11, -11, -11, -6, -5, -5, -5, -5, -4, -1, 0, 2, 2, 2, 2, 5, 6, 7, 7, 9, 10, 13, 13, 14, 14, 18, 21, 21, 21, 22, 24, 24, 24, 25, 26, 26, 29, 29, 29, 30, 30, 31, 31, 32, 33, 34, 34, 34, 35, 38, 40, 41, 42, 43, 44, 44, 46, 46, 47, 47, 48, 49, 49]
"""
from typing import List
import doctest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # noqa
        nums2.extend(nums1[0:m])
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
        nums1.sort()
        return nums1


doctest.testmod()
