# climb letters
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""最简单的dp, status function:dp[i] = dp[i-1] + dp[i-2]"""
"""相关题目：min cost climbing stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
