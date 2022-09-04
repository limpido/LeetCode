class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        dp[i, j]: number of palindromic substrings
        dp[i, j] = dp[i+1, j] + dp[i, j-1] - dp[i+1][j-1] + (1 if isPalindrome[i][j] else 0)
        '''
        '''
        palindrome = [[0]*len(s) for _ in range(len(s))]
        dp = [[0]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            palindrome[i][i] = True
            for j in range(i+1, len(s)):
                palindrome[i][j] = s[i] == s[j] if j == i+1 else (s[i] == s[j] and palindrome[i+1][j-1])
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + (1 if palindrome[i][j] else 0)
                
        return dp[0][len(s)-1]
        '''
        
    
        '''
        count palindromic substrings
        dp[i, j]: whether substring[i, j] is palindrome
        '''
        dp = [[0]*len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] if j <= i+1 else (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j]:
                    res += 1
                
        return res