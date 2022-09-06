class Solution:
    def isHappy(self, n: int) -> bool:
        # s = set()
        # while True:
        #     total = 0
        #     while n > 0:
        #         n, total = n // 10, total + (n % 10) ** 2
        #     if total == 1:
        #         return True
        #     elif total in s:
        #         return False
        #     s.add(total)
        #     n = total
        
        seen = set()
        while True:
            s = 0
            for ch in str(n):
                s += int(ch) ** 2
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            n = s