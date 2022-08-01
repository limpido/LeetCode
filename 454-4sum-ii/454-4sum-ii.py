class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        
        for n3 in nums3:
            for n4 in nums4:
                if -(n3+n4) in hashmap:
                    res += hashmap[-(n3+n4)]
        return res