class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        idx = []
        chs = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                idx.append(i)
                chs.append(s[i])
        i, j = 0, len(chs)-1
        res = list(s)
        while j >= 0:
            res[idx[i]] = chs[j]
            i += 1
            j -= 1
        return ''.join(res)