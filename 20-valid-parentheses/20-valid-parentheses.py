class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for bracket in s:
            if bracket in dic:
                stack.append(bracket)
            else:
                if len(stack) == 0 or dic[stack.pop()] != bracket:
                    return False
        return len(stack) == 0