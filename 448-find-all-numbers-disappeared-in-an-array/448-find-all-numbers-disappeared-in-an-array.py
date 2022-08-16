class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
                