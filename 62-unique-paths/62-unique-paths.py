class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp[i, j]: number of unique paths to reach the bottom right starting from the position i, j
        dp[i, j] = dp[i+1, j] + dp[i, j+1]
        '''
        '''method 1: 2d array'''
        # dp = [[0] * n for i in range(m)]
        # dp[m-1][n-1] = 1
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i+1 < m:
        #             dp[i][j] += dp[i+1][j]
        #         if j+1 < n:
        #             dp[i][j] += dp[i][j+1]
        # return dp[0][0]
        
        '''method 2: 1d array'''
        dp = [1] * m
        for i in range(0, n-1):
            for j in range(m-2, -1, -1):
                dp[j] = dp[j] + dp[j+1]
        return dp[0]