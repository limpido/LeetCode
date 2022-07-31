class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        left, right = 0, len(nums)-1
        i = len(nums)-1
        while i >= 0:
            if nums[left] ** 2 > nums[right] ** 2:
                res[i] = nums[left] ** 2
                left += 1
                i -= 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
                i -= 1
        return res