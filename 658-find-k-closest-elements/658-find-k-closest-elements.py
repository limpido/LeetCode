class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorted, may have duplicates, x may not exist in the array
        def right_dist(idx):
            return arr[idx]-x
        
        def left_dist(idx):
            return x-arr[idx]
        
        res = []
        
        idx = 0
        while idx < len(arr):
            if x <= arr[idx]:
                break
            idx += 1
        
        idx = min(len(arr)-1, idx)
        
        l, r = idx-1, idx
        while k > 0 and r < len(arr) and l >= 0:
            rd = right_dist(r)
            ld = left_dist(l)
            if rd < ld:
                res.append(arr[r])
                r += 1
            else:
                res.insert(0, arr[l])
                l -= 1
            k -= 1
        while k > 0 and r < len(arr):
            res.append(arr[r])
            r += 1
            k -= 1
        while k > 0 and l >= 0:
            res.insert(0, arr[l])
            l -= 1
            k -= 1
        
        return res