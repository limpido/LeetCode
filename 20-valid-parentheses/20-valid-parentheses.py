class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            else:
                if bracket == ')' and stack[-1] == '(':
                    stack.pop()
                elif bracket == '}' and stack[-1] == '{':
                    stack.pop()
                elif bracket == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False