class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        i = 0
        isNegative = False
        
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "-":
            isNegative = True
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        
        while i < len(s):
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                break
            else:
                num = num*10 + ord(s[i])-ord('0')
                i += 1
            
        return min(num, 2**31-1) if not isNegative else max(-num, -2**31)