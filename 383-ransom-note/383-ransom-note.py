class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for ch in magazine:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
        for ch in ransomNote:
            if ch not in hashmap or hashmap[ch] == 0:
                return False
            hashmap[ch] -= 1
        return True