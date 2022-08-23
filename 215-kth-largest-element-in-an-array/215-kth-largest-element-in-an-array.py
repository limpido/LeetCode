import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:      
        def partition(left, right):
            pivot = nums[right]
            bound = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[bound] = nums[bound], nums[i]
                    bound += 1
            nums[right], nums[bound] = nums[bound], nums[right]
            return bound
        
        target_idx = len(nums) - k
        left, right = 0, len(nums)-1
        while left <= right:
            idx = partition(left, right)
            if idx == target_idx:
                return nums[idx]
            elif idx < target_idx:
                left = idx+1
            else:
                right = idx-1
