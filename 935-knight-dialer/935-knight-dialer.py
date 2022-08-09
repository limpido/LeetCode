class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        dp[i, n]: the number of distinct phone numbers of length n, starting from i
        dp[i, n] = sum{dp[neighbors[i], n-1]}
        '''
        if n == 1:
            return 10
        
        neighbors = {
            1: (6, 8), 
            2: (7, 9), 
            3: (4, 8), 
            4: (3, 9, 0),
            5: tuple(),
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6)
        }
        
        prev = [1] * 10
        
        for k in range(2, n+1):
            cur = [0] * 10
            for i in range(10):
                for neighbor in neighbors[i]:
                    cur[i] += prev[neighbor]
            prev = cur
        
        return sum(cur) % (10**9 + 7)