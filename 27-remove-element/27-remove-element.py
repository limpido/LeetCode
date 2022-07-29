class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] == val else 1
        left, right = 0, len(nums)-1
        while left < right:
            while left < right and nums[left] != val:
                left += 1
            while left < right and nums[right] == val:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return left if nums[left] == val else left+1