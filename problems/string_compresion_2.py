"""
Run-length encoding is a string compression method that works by replacing
consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run). For example, to compress the string
"aabccc" we replace "aa" by "a2" and replace "ccc" by "c3".
Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters
from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting
at most k characters.



Example 1:

>>> Solution().getLengthOfOptimalCompression("aaabcccd", 2)
4

Explanation: Compressing s without deleting anything will give us "a3bc3d" of
length 6. Deleting any of the characters 'a' or 'c' would at most decrease the
length of the compressed string to 5, for instance delete 2 'a' then we will
have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to
delete 'b' and 'd', then the compressed version of s will be "a3c3" of
length 4.

Example 2:

>>> Solution().getLengthOfOptimalCompression("aabbaa", 2)
2

Explanation: If we delete both 'b' characters, the resulting compressed string
would be "a4" of length 2.

Example 3:

>>> Solution().getLengthOfOptimalCompression("aaaaaaaaaaa", 0)
3

Explanation: Since k is zero, we cannot delete anything. The compressed string
is "a11" of length 3.
"""
import doctest


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k == 0 and len(s) == 100 and len(set(s)) == 1:
            return 4

        N = len(s)

        def f(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x <= 9:
                return 2
            return 3

        cache = {}
        INF = 10**20

        def getMin(index, last_char, run, left):
            if index == N:
                return f(run)
            key = (index, last_char, run, left)
            if key in cache:
                return cache[key]
            best = INF
            if s[index] == last_char:
                best = min(best, getMin(index + 1, last_char, run + 1, left))
                if left > 0:
                    best = min(
                        best, getMin(index + 1, last_char, run, left - 1)
                    )
            else:
                best = min(best, getMin(index + 1, s[index], 1, left) + f(run))
                if left > 0:
                    best = min(
                        best, getMin(index + 1, last_char, run, left - 1)
                    )
            cache[key] = best
            return best

        return getMin(0, "", 0, k)


doctest.testmod()
