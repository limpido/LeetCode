class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        idx = []
        chs = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                idx.append(i)
                chs.append(s[i])
        i = 0
        res = list(s)
        chs.reverse()
        while i < len(idx):
            res[idx[i]] = chs[i]
            i += 1
        return ''.join(res)