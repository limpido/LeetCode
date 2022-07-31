class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            arr = [0] * 26
            for ch in str:
                arr[ord(ch) - ord('a')] += 1
            d[tuple(arr)] = d.get(tuple(arr), []) + [str]
        return list(d.values())