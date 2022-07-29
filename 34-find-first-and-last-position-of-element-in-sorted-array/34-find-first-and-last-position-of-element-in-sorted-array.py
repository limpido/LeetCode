class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        res = []
        
        # binary search left border
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
                
        if left < len(nums) and nums[left] == target:
            res.append(left)
        else: return [-1, -1]
        
        # binary search right border
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        res.append(right)
        return res
        