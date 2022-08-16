class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ''' Method 1: Cyclic Sort        
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i]-1
                if nums[j] != nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                else: i += 1
            else:
                i += 1
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res
        '''
        
        '''Method 2: Negative Marking
        for each number n, mark the element at the index n-1 as negative
        if an element n is positive, meaning that the number n+1 does not exist in the array
        '''
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res