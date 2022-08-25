class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(cur, left, right):
            if len(cur) == n*2:
                res.append(''.join(cur))
                return
            
            if left < n:
                cur.append('(')
                backtrack(cur, left+1, right)
                cur.pop()

            if right < left:
                cur.append(')')
                backtrack(cur, left, right+1)
                cur.pop()
                
        
        backtrack([], 0, 0)
        return res