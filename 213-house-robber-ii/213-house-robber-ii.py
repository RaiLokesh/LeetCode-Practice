class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums1 = nums[1:]
        nums = nums[:len(nums)-1]
        x = y = 0
        if len(nums) == 1:
            x = nums[0]
        else:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = nums[1]
            for i in range(2, len(nums)):
                for j in range(0, i-1):
                    dp[i] = max(dp[i], nums[i] + dp[j])
            x = (max(dp[-1], dp[-2]))
        if len(nums1) == 1:
            y = nums1[0]
        else:
            dp = [0]*len(nums1)
            dp[0] = nums1[0]
            dp[1] = nums1[1]
            for i in range(2, len(nums1)):
                for j in range(0, i-1):
                    dp[i] = max(dp[i], nums1[i] + dp[j])
            y = (max(dp[-1], dp[-2]))
        return max(x, y)