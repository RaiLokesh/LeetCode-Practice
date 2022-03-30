class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = (nums[i]-1) % len(nums)
            nums[x] = nums[x] + len(nums)
            
        for i in range(len(nums)):
            if nums[i] > 2*(len(nums)):
                return i + 1
            