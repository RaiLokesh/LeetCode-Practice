class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = [0]*len(nums)
        i = j = 1
        count = 1
        while i < len(nums):
            if nums[i] == nums[j-1]:
                if count < 2:
                    nums[j] = nums[i]
                    j += 1
                    count += 1
            else:
                nums[j] = nums[i]
                j += 1
                count = 1
            i += 1
        return j
                