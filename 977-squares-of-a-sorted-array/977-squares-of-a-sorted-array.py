class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        left, right = i-1, i
        while left >=0 and right < len(nums):
            if nums[left] ** 2 < nums[right] ** 2:
                res.append(nums[left] ** 2)
                left -= 1
            else:
                res.append(nums[right] ** 2)
                right += 1
        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1
        while right < len(nums):
            res.append(nums[right] ** 2)
            right += 1
        return res