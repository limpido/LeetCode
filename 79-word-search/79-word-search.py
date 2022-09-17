class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        
        def dfs(r, c, idx, visited):
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[idx]:
                return False
            
            if idx == len(word)-1:
                return True
            
            visited.add((r, c))
            
            if not (dfs(r, c+1, idx+1, visited) or dfs(r, c-1, idx+1, visited) or dfs(r+1, c, idx+1, visited) or dfs(r-1, c, idx+1, visited)):
                visited.remove((r, c))
                return False
            return True
            
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, 0, visited):
                        return True
                    
        return False