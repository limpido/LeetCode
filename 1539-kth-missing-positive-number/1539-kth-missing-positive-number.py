class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''Method 1: O(n)
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
        '''
        
        '''Method 2: Set
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set: k -= 1
            if k == 0: return i
        '''
        
        '''Method 3: O(logn) binary search
        amount of missing numbers before arr[i]: arr[i]-i-1
        '''
        l, r = 0, len(arr)-1
        while l < r:
            mid = (l+r) // 2
            missing_num = arr[mid]-mid-1
            if missing_num < k:
                l = mid+1
            else:
                r = mid-1
        
        missing_num = arr[l]-l-1
        if missing_num >= k:
            k = missing_num - k + 1
            return arr[l] - k
        else:
            k = k - missing_num
            return arr[l]+k