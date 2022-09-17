class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                start = i
                while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == len(needle):
                    return start
                else:
                    i = start+1
                    j = 0
            else:
                i += 1
        return -1