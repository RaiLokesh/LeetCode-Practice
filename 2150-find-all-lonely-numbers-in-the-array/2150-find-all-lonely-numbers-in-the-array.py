class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        nums.sort()
        count = []
        for i in range(len(nums)):
            if i==0:
                if nums[i]+1 != nums[i+1] and nums[i]!=nums[i+1]:
                    count.append(nums[i])
            elif i==len(nums)-1:
                if nums[i] != nums[i-1]+1 and nums[i]!=nums[i-1]:
                    count.append(nums[i])
            else:
                if nums[i]+1 != nums[i+1] and nums[i] != nums[i-1]+1 and nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                    count.append(nums[i])
        return count