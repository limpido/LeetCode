class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        dp[i]: max sum of subarray until the index i
        dp[i] = dp[i-1] > 0 ? dp[i-1]+nums[i] : nums[i]
        '''
        dp = [nums[0]]
        max_total = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                total = dp[i-1]+nums[i]
                dp.append(total)
                max_total = max(max_total, total)
            else:
                dp.append(nums[i])
                max_total = max(max_total, nums[i])
        return max_total