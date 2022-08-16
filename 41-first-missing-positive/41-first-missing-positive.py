class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        1. brute force: sort O(nlogn)
        '''
        '''2. extra memory
        arr_set = set(nums)
        i = 1
        while True:
            if i in arr_set:
                i += 1
            else:
                return i
        '''
        
        '''3. cyclic sort'''
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != i+1:
                j = nums[i]-1
                if nums[i] == nums[j]:
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1