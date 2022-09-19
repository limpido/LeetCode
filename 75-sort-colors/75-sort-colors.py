class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''method 1: bubble sort, O(n^2)'''
        # for j in range(len(nums)):
        #     for i in range(len(nums)-1):
        #         if nums[i] > nums[i+1]:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
            
        '''method 2: count sort'''
        count = [0]*3
        for n in nums:
            count[n] += 1
        
        p = 0
        for i in range(len(nums)):
            while p < len(count) and count[p] == 0:
                p += 1
            if p == len(count):
                break
            
            nums[i] = p
            count[p] -= 1
            
        
        
        
        