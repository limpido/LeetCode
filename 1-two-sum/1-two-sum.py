class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            peer = target-nums[i]
            if peer in d:
                return[d[peer], i]
            else:
                d[nums[i]] = i