class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        dp[i, j]: longest palindromic subsequence's length between i and j
        1. s[i] == s[j]  dp[i, j] = dp[i+1, j-1]+2
        2. s[i] != s[j]  dp[i, j] = max(dp[i+1, j], dp[i, j-1])
        '''
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return 2 if s[0] == s[1] else 1
        
        res = 1
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                res = max(res, dp[i][j])

        return res