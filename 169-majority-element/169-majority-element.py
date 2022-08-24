class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''Boyer-Moore Voting'''
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        
        return candidate