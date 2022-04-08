class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            arr = []
            for i in range(1, len(nums)):
                arr.append((nums[i]+nums[i-1])%10)
            nums = arr
        return nums[0]