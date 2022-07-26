class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(arr):
            start, end = 0, len(arr)-1
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            return arr
        
        arr = list(s)
        for i in range(0, len(arr), 2*k):
            arr[i:i+k] = reverse(arr[i:i+k])
        return ''.join(arr)