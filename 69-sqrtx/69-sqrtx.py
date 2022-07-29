class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 2, x // 2
        while left <= right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid+1
            elif mid * mid > x:
                right = mid-1
        return right