class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''method 1: stack'''
        # stack = []
        # for ch in s:
        #     if len(stack) == 0 or stack[-1] != ch:
        #         stack.append(ch)
        #     else:
        #         stack.pop()
        # return "".join(stack)
        
        '''method 2: two pointers'''
        res = list(s)
        slow = fast = 0

        while fast < len(res):
            res[slow] = res[fast]
            
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])