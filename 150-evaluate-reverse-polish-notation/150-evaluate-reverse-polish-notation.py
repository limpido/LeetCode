class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": add, "-": sub, "*": mul, "/": truediv}
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                op = operators[t]
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                res = op(value1, value2)
                stack.append(int(res))
        return int(stack.pop())