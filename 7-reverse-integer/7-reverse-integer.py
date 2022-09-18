class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        if isNegative:
            x = -x
        
        res = 0
        while x > 0:
            res = res * 10 + x%10
            x = x // 10
        if isNegative:
            res = -res
        if res < -2**31 or res > 2**31-1:
            return 0
        return res