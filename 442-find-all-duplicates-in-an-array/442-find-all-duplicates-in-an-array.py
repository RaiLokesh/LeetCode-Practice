class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[(nums[i]-1)%len(nums)] = nums[(nums[i]-1)%len(nums)] + len(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] > 2*len(nums):
                ans.append(i+1)
        return ans