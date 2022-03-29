class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(len(nums)):
            maxi = max(maxi, nums[i]+nums[~i])
        return maxi