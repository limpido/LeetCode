class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorted, may have duplicates, x may not exist in the array
        idx = 0
        while idx < len(arr):
            if x <= arr[idx]:
                break
            idx += 1
        
        idx = min(len(arr)-1, idx)
        
        l, r = idx-1, idx
        while k > 0:
            if r >= len(arr) or l >= 0 and x-arr[l] <= arr[r]-x:
                l -= 1
            else:
                r += 1
            
            k -= 1
        
        return arr[l+1:r]