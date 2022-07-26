class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        arr = list(s)
        for i in range(0, len(arr), 2*k):
            end = i+k-1 if i+k-1 < len(arr) else len(arr)-1
            reverse(arr, i, end)
        return ''.join(arr)