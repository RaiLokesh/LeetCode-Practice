class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                nums[-1] = '_'
            else: i += 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == '_': return count
            count += 1
            