class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            for j in range(0, i-1):
                dp[i] = max(dp[i], nums[i] + dp[j])
        return(max(dp[-1], dp[-2]))