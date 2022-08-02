class Solution:
    def climbStairs(self, n: int) -> int:
        '''dp[n] = dp[n-1] + dp[n-2]'''
        dp = [1, 2]
        if n <= 2:
            return dp[n-1]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]