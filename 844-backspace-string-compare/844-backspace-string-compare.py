class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sarr = ['']*len(s)
        i = 0
        for c in s:
            if c == '#':
                i -= 1
                i = max(0, i)
            else:
                sarr[i] = c
                i += 1
        sres = ''.join(sarr[:i])
        
        tarr = ['']*len(t)
        i = 0
        for c in t:
            if c == '#':
                i -= 1
                i = max(0, i)
            else:
                tarr[i] = c
                i += 1
        tres = ''.join(tarr[:i])
        return sres == tres