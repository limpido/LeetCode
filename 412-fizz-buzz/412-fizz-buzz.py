class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        ans = []
        
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                ans.append("FizzBuzz")
            elif i%3 == 0:
                ans.append("Fizz")
            elif i%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
        '''
        
        ans = []
        for i in range(1, n+1):
            s = ""
            if i%3 == 0:
                s += "Fizz"
            if i%5 == 0:
                s += "Buzz"
            if not s:
                s = str(i)
            ans.append(s)
        return ans