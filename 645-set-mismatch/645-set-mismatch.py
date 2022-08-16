class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i]-1
                if nums[i] == nums[j]:
                    if not res:
                        res.append(nums[i])
                    i += 1
                else:
                    nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res