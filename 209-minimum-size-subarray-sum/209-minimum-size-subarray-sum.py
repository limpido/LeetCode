class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        total = nums[left]
        res = 0
        while right < len(nums):
            if total < target:
                right += 1
                if right < len(nums):
                    total += nums[right]
            else:
                res = right-left+1 if res == 0 else min(res, right-left+1)
                if res == 1: break
                if total == target:
                    right += 1
                    if right < len(nums):
                        total += nums[right]
                total -= nums[left]
                left += 1
        return res