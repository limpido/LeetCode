class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        dp[i, j] = dp[i+1, j-1] and s[i] == s[j]
        '''
        
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        
        dp = [[0] * len(s) for _ in range(len(s))]
        res = [0,0]
        maxLen = 1
        
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, len(s)):
                if j == i+1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i+1 > maxLen:
                    res = [i, j]
                    maxLen = j-i+1
        return s[res[0]: res[1]+1]