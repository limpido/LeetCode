import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' Method 1: min heap
        
        map_ = {}  # frequency of nums
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        pri_que = []  # min heap
        
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
        '''
        
        ''' Method 2: bucket sort'''
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key in hm.keys():
            bucket[hm[key]].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if len(bucket[i]):
                res.extend(bucket[i])
            if len(res) == k:
                return res
