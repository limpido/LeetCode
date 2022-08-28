class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=lambda s: len(s))
        if len(shortest) == 0:
            return ""
        
        res = ""
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] != strs[j][i]:
                    return res
            res += shortest[i]
        return res