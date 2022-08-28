class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        0/1 knapsack
        
        Method 1: 2d dp
        dp[i][j]: whether the sum j can be gotten from the first i numbers
        1. pick nums[i]: dp[i][j] = dp[i-1][j-nums[i]]
        2. not pick nums[i]: dp[i][j] = dp[i-1][j]
        dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        
        total = sum(nums)
        if total%2 == 1:
            return False
        
        n = len(nums)
        
        total = total // 2
        dp = [[False]*(total+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1, n+1):
            for j in range(1, total+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][total]
        '''
        
        '''Method 2: 1d dp'''
        total = sum(nums)
        if total%2 == 1:
            return False
        
        total = total // 2
        dp = [False]*(total+1)
        dp[0] = True
        
        for num in nums:
            for i in range(total, 0, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i-num]
                
        return dp[total]
        