class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        res = []
        
        arr.sort()
        
        for num in arr:
            d.setdefault(bin(num).count('1'), [])
            d.get(bin(num).count('1')).append(num)
        
        for bits, val in sorted(d.items(), key=lambda x: x[0]):   # sort by dict key, which is the number of bit '1'
            res += val
        
        return res