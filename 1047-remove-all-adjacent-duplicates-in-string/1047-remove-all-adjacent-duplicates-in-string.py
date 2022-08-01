class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) == 0 or stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)