class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        check = nums[0]
        for i in range(1, len(nums)):
            if nums[i]!=check:
                count = 1
                check = nums[i]
            else:
                count += 1
                if count > 2:
                    nums[i] = float('inf')
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == float('inf'):
                return i
        