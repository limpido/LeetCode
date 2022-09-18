class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        
        def backtrack(cur, idx):
            if idx == len(digits):
                res.append("".join(cur))
                return
            
            characters = d[int(digits[idx])]
            for c in characters:
                cur.append(c)
                backtrack(cur[:], idx+1)
                cur.pop()
                
        backtrack([], 0)
        return res