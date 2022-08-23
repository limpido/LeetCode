class Solution:
    def frequencySort(self, s: str) -> str:
        '''bucket sort'''
        bucket = [[] for _ in range(len(s)+1)]
        hm = {}
        for ch in s:
            hm[ch] = hm.get(ch, 0)+1
        
        for key in hm.keys():
            bucket[hm[key]].append(key)
        
        res = ""
        for i in range(len(bucket)-1, -1, -1):
            if len(bucket[i]):
                for ch in bucket[i]:
                    for _ in range(i):
                        res += ch
        return res