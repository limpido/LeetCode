class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        count = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count