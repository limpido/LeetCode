class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        arr = list(s)
        start, end = 0, len(arr)-1
        
        while start < end:
            while start < end and arr[start].lower() not in vowels:
                start += 1
            while start < end and arr[end].lower() not in vowels:
                end -= 1
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return ''.join(arr)