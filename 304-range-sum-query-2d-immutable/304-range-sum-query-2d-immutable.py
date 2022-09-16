class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.dp = [[0]*(C+1) for _ in range(R+1)]
        for r in range(1, R+1):
            for c in range(1, C+1):
                self.dp[r][c] = self.dp[r-1][c] + self.dp[r][c-1] - self.dp[r-1][c-1] + matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.dp[r2][c2] - self.dp[r1-1][c2] - self.dp[r2][c1-1] + self.dp[r1-1][c1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)