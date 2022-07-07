import bisect
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot = nums[i-1]
                dontChangeList = nums[:i-1]
                check = 0
                for j in range(len(nums[i-1:])-1, -1, -1):
                    if nums[i-1:][j] > pivot:
                        check = i+j-1; break
                sort = sorted(nums[i-1:check])
                k = dontChangeList + [nums[check]] + sorted(nums[check+1:]) + sort
                for i in range(len(k)):
                    nums[i] = k[i]
                break
        else:
            k = nums[::-1]
            for i in range(len(nums)):
                nums[i] = k[i]