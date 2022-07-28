class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
        for f in freq:
            if f != 0:
                return False
        return True