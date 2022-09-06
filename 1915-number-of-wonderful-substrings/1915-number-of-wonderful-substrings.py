class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        '''
        word contains the first ten characters
        the largest state is 11111 11111
        2^10 = 1024
        '''

        mask = 0  # current state
        count = [0] * 1024  # count how many times the state occurs
        count[0] = 1
        res = 0
        
        for ch in word:
            idx = ord(ch) - ord('a')
            mask = mask ^ (1 << idx)
            res += count[mask]
            for i in range(10):
                look_for_state = mask ^ (1 << i)
                res += count[look_for_state]
            count[mask] += 1
        return res