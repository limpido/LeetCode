class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 = n1*10 + ord(num1[i])-ord("0")
        for i in range(len(num2)):
            n2 = n2*10 + ord(num2[i])-ord("0")
        return str(n1*n2)