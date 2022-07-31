class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        count = 1
        
        layer = (n+1) // 2
        for l in range(layer):
            for i in range(l, n-l):
                res[l][i] = count
                count += 1
            
            for i in range(l+1, n-l):
                res[i][n-l-1] = count
                count += 1
            
            for i in range(n-l-2, l-1, -1):
                res[n-l-1][i] = count
                count += 1
            
            for i in range(n-l-2, l, -1):
                res[i][l] = count
                count += 1
        
        return res