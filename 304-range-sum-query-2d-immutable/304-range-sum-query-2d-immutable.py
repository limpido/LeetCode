class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[row[0]] for row in matrix]
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(1, C):
                self.prefix[r].append(self.prefix[r][c-1] + matrix[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2+1):
            res += self.prefix[r][col2]-self.prefix[r][col1] + self.matrix[r][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)