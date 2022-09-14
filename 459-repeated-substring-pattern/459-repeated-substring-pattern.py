class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''Method 1'''
        # ss = (s + s)[1:-1]
        # return ss.find(s) != -1
        
        '''Method 2'''
        n = len(s)
        for i in range(1, n//2+1):
            if n % i == 0 and s[:i]* (n//i) == s:
                return True
        return False