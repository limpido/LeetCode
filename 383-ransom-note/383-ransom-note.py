class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0]*26
        for ch in magazine:
            arr[ord(ch)-ord('a')] += 1
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if arr[idx] == 0:
                return False
            arr[idx] -= 1
        return True