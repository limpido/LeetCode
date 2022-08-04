class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(cur, start):
            if len(cur) == k:
                res.append(cur[:])
            for i in range(start, n+1):
                cur.append(i)
                backtrack(cur, i+1)
                cur.pop()
            
        backtrack([], 1)
        return res