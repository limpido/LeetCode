class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''Method 1: bucket sort'''
        '''
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
        '''
        
        '''Method 2: priority queue / min heap'''
        hp = list(collections.Counter(arr).values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
        return len(hp) + (k < 0)