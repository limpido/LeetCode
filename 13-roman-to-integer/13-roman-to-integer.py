class Solution:
    def romanToInt(self, s: str) -> int:
        prefix = {
            "V": "I",
            "X": "I",
            "L": "X",
            "C": "X",
            "D": "C",
            "M": "C"
        }
        
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        i = len(s)-1
        res = 0
        
        while i >= 0:
            if i >= 1 and s[i] in prefix and s[i-1] == prefix[s[i]]:
                res += value[s[i]] - value[s[i-1]]
                i -= 2
            else:
                res += value[s[i]]
                i -= 1
                
        return res