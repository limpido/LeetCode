class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = 0
        count = 0
        prod = 1
        while r < len(nums):
            prod *= nums[r]
            while prod >= k and l <= r:
                prod = prod // nums[l]
                l += 1
            count += r-l+1
            r += 1
        return count