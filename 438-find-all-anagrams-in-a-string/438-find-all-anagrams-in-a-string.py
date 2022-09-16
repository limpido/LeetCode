class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = {}
        for ch in p:
            count[ch] = count.get(ch, 0)+1
        
        res = []
        l = 0
        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0)-1
            while count[ch] < 0:
                count[s[l]] += 1
                l += 1
            if r-l+1 == len(p):
                res.append(l)
        return res
        
            