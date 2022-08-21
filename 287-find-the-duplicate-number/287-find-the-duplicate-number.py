class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i]-1
                if nums[j] == nums[i]:
                    return nums[i]
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1