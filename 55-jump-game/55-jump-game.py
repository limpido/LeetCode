class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        method 1
        '''
        last_pos = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= last_pos-i:
                last_pos = i
        return last_pos == 0
        
        '''
        method 2: max position so far, O(n)
        '''
        # max_pos = 0
        # i = 0
        # while i <= max_pos:
        #     max_pos = max(max_pos, nums[i]+i)
        #     if max_pos >= len(nums)-1:
        #         return True
        #     i += 1
        # return False