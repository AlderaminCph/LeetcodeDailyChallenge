"""
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

>>> canConstruct("a","b")
False

Example 2:

>>> canConstruct("aa","ab")
False

Example 3:

>>> canConstruct("aa","aab")
True
"""
import doctest
from collections import defaultdict


def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(magazine) < len(ransomNote):
        return False
    ransom_dict = defaultdict(int)
    for char in ransomNote:
        ransom_dict[char] += 1
    if all(ransom_dict[char] <= magazine.count(char) for char in ransom_dict):
        return True
    return False


doctest.testmod()
