class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 1: return nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if i == 1: return nums[0]
                if i+1 == len(nums) or (i+1 < len(nums) and nums[i] != nums[i+1]):
                    return nums[i]