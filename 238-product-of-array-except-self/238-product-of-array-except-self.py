class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        start = 1
        for i in range(len(nums)):
            prod.append(start)
            start *= nums[i]
        start = 1
        for i in range(len(nums)):
            prod[~i] = start*prod[~i]
            start *= nums[~i]
        
        return prod