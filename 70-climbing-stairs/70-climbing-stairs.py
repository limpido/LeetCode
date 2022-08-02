class Solution:
    def climbStairs(self, n: int) -> int:
        '''dp[n] = dp[n-1] + dp[n-2]'''
        if n <= 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]