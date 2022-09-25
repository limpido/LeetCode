class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        row 0: 0, 6, 12  n*2-2
        row 1: 1, 5, 7, 11, 13
        row 2: 2, 4, 8
        row 3: 3, 9
        
        row k: k, (n-r)*2-2, r*2
        '''
    
        if numRows == 1:
            return s
        
        res = ""
        
        for r in range(numRows):
            k = r
            if r == 0 or r == numRows-1:
                while k < len(s):
                    res += s[k]
                    k += numRows*2-2
                
            else:
                count = 1
                while 0 <= k < len(s):
                    res += s[k]
                    if count % 2 == 1:
                        k += (numRows-r)*2-2
                    elif count % 2 == 0:
                        k += r*2

                    count += 1
        return res
                    
        