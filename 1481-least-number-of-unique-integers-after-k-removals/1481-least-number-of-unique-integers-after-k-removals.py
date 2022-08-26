class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        bucket = [[] for _ in range(len(arr)+1)]
        freq = {}
        for n in arr:
            freq[n] = freq.get(n, 0)+1
        for n, f in freq.items():
            bucket[f].append(n)
        
        s = set(arr)
        i = 0
        while k > 0:
            while len(bucket[i]) == 0:
                i += 1
            n = bucket[i].pop()
            if k >= i:
                s.remove(n)
            k -= i
        return len(s)