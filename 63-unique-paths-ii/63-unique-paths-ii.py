class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        dp[i, j] = dp[i+1, j] + dp[i, j+1]
        '''
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[row-1][col-1] == 1: return 0
        dp = [[0] * col for _ in range(row)]
        dp[row-1][col-1] = 1
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i+1 < row and obstacleGrid[i+1][j] == 0:
                    dp[i][j] += dp[i+1][j]
                if j+1 < col and obstacleGrid[i][j+1] == 0:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]