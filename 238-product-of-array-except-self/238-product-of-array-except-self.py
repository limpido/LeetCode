class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            left.append(product)
        
        right = 1
        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            left[i] = left[i]*right
        
        return left