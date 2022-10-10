"""
Given a palindromic string of lowercase English letters palindrome, replace
exactly one character with any lowercase English letter so that the resulting
string is not a palindrome and that it is the lexicographically smallest one
possible.

Return the resulting string. If there is no way to replace a character to make
it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if
 in the first position where a and b differ, a has a character strictly smaller
  than the corresponding character in b. For example, "abcc" is
  lexicographically smaller than "abcd" because the first position they differ
  is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

>>> Solution().breakPalindrome("abccba")
"aaccba"

Explanation: There are many ways to make "abccba" not a palindrome,
such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:

>>> Solution().breakPalindrome("a")
""

Explanation: There is no way to replace a single character to make "a" not a
palindrome, so return an empty string.

"""
import doctest


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        letters = list(palindrome)  # in order to be able to change letters
        mid = len(palindrome) // 2
        # change the first non 'a' to 'a'
        for i in range(mid):
            if letters[i] != "a":
                letters[i] = "a"
                return "".join(letters)
        # if there are no non 'a'
        letters[-1] = "b"
        return "".join(letters)

doctest.testmod()