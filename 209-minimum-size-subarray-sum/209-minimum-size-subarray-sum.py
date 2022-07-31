class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left, right = 0, 0
        res = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                res = right-left+1 if res == 0 else min(res, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return res