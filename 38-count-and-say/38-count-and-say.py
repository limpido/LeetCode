class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s):
            res = []
            count = 1
            for i in range(1, len(s)):
                if s[i] != s[i-1]:
                    res.append([count, s[i-1]])
                    count = 1
                else:
                    count += 1
            res.append([count, s[-1]])
            return res
        
        def say(arr):
            res = ""
            for pair in arr:
                res += "".join([str(item) for item in pair])
            return res
        
        s = "1"
        for i in range(1, n):
            s = say(count(s))
        return s