class Solution:
    def fib(self, n: int) -> int:
        '''method 1: recursion'''
        # if n <= 1: return n
        # return self.fib(n-1) + self.fib(n-2)
    
        '''method 2: dp'''
        # if n <= 1: return n
        # dp = [0, 1]
        # for i in range(2, n+1):
        #     dp.append(dp[i-1] + dp[i-2])
        # return dp[n]
        
        '''method 3: dp space O(1)'''
        if n <= 1: return n
        fib1, fib2 = 0, 1
        for i in range(2, n+1):
            fib3 = fib1+fib2
            fib1, fib2 = fib2, fib3
        return fib3