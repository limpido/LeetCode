class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i]-1
                if nums[j] == nums[i]:
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
        return res