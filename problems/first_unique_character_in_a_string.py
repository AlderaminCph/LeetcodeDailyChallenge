"""
Given a string s, find the first non-repeating character in it and return its
index. If it does not exist, return -1.



Example 1:

>>> firstUniqChar("leetcode")
0

Example 2:

>>> firstUniqChar("loveleetcode")
2

Example 3:

>>> firstUniqChar("aabb")
-1
"""
import doctest
from collections import defaultdict


def firstUniqChar(s: str) -> int:
    repeats = defaultdict(int)
    for char in s:
        repeats[char] += 1
    for char in repeats:
        if repeats[char] == 1:
            return s.index(char)
    return -1


doctest.testmod()
