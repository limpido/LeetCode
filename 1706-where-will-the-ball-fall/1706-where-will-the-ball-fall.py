class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        '''
        stuck:
        grid[r][c] * grid[r][c+1] == -1
        '''
        ROW, COL = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r >= ROW:
                return c
            if c == 0 and grid[r][c] == -1 or c == COL-1 and grid[r][c] == 1:
                return -1
            elif grid[r][c] == 1 and grid[r][c+1] == -1:
                return -1
            elif grid[r][c] == -1 and grid[r][c-1] == 1:
                return -1
            
            if grid[r][c] == 1:
                return dfs(r+1, c+1)
            else:
                return dfs(r+1, c-1)
        
        
        answer = []
        for c in range(COL):
            answer.append(dfs(0, c))            
        return answer