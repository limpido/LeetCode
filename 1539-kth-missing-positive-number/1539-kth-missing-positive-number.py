class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''Method 1: O(n)'''
        miss = []
        i = 0
        n = 1
        while i < len(arr):
            if arr[i] != n:
                miss.append(n)
            else:
                i += 1
            n += 1
            
        return miss[k-1] if len(miss) >= k else arr[-1]+ k-len(miss)