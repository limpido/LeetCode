class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = len(s)-1

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0:
            if s[i] == " ":
                return res
            res += 1
            i -= 1
        return res