class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        start, end = 0, len(words)-1
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1
        return ' '.join(words)