"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job
schedule is the sum of difficulties of each day of the d days.
The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty
of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule
for the jobs return -1.



Example 1:

>>> Solution().minDifficulty([6,5,4,3,2,1], 2)
7

Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

Example 2:

>>> Solution().minDifficulty([9,9,9], 4)
-1

Explanation: If you finish a job per day you will still have a free day. you
cannot find a schedule for the given jobs.

Example 3:

>>> Solution().minDifficulty([1,1,1], 3)
3

Explanation: The schedule is one job per day. total difficulty will be 3.
"""
from typing import List
import sys
from functools import lru_cache
import doctest


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        @lru_cache(None)
        def dp(index, remain_days):
            if remain_days == 0 and index == 0 or index == n and  remain_days == 0:
                return 0  # valid scenario
            elif remain_days == 0 and index != n or index == n and remain_days != 0:
                return sys.maxsize  # invalid

            ans = sys.maxsize
            current_max = 0
            for i in range(index, n):
                current_max = max(current_max, jobDifficulty[i])
                ans = min(ans, current_max + dp(i + 1, remain_days - 1))

            return ans

        return dp(0, d)
doctest.testmod()