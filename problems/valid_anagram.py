"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
 word or phrase, typically using all the original letters exactly once.



Example 1:

>>> isAnagram("anagram","nagaram")
True

Example 2:

>>> isAnagram("rat", "car")
False
"""
import doctest


def isAnagram(s: str, t: str) -> bool:
    if len(set(s)) == len(set(t)):
        if all(s.count(char) == t.count(char) for char in set(s)):
            return True
    return False


doctest.testmod()
