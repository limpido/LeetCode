class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == 'X' or board[r][c] == '#':
                return
            board[r][c] = '#'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            
        ROW = len(board)
        COL = len(board[0])
        
        for i in [0, ROW-1]:
            for j in range(COL):
                if board[i][j] == 'O':
                    dfs(i, j)   
        for i in range(ROW):
            for j in [0, COL-1]:
                if board[i][j] == 'O':
                    dfs(i, j)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'