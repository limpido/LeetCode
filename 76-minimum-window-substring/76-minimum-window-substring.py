class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreq = {}  # frequency of characters in t
        required = 0  # the number of unique characters in t
        for ch in t:
            if ch in tFreq:
                tFreq[ch] += 1
            else:
                tFreq[ch] = 1
                required += 1
        
        left, right = 0, 0
        match = 0   # the number of unique characters in s that match the frequency in t
        window = {}  # frequency of characters in the current window
        res = None
        
        while right < len(s):
            ch = s[right]
            if ch in window:
                window[ch] += 1
            else: window[ch] = 1
            
            if ch in tFreq and window[ch] == tFreq[ch]:
                match += 1
            
            while left <= right and match == required:
                if res is None or right-left+1 < len(res):
                    res = s[left:right+1]
                
                ch = s[left]
                window[ch] -= 1
                if ch in tFreq and window[ch] < tFreq[ch]:
                    match -= 1
                left += 1
            
            right += 1
        return "" if res is None else res
        