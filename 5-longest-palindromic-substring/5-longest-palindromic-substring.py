class Solution:
    def longestPalindrome(self, s: str) -> str:
        ''' Method 1: DP
        dp[i, j]: whether the substring between the index i and j is palindrome
        dp[i, j] = dp[i+1, j-1] and s[i] == s[j]

        
        if len(s) == 1: return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        
        dp = [[0]*len(s) for _ in range(len(s))]
        max_length = 1
        res = s[0]
        
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, len(s)):
                if j == i+1: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    res = s[i:j+1]
        return res
        '''
        
        '''Method 2: Expand Around Center'''
        def expandAroundCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r-l-1   # r-1 - (l+1) + 1 = r-l-1
        
        if len(s) == 1: return s
        l, r = 0, 0
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i+1)
            length = max(odd, even)
            if length > r-l+1:
                l = i- (length-1) // 2
                r = i+ length // 2
        return s[l:r+1]