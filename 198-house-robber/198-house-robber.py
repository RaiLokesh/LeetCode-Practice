class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        if len(nums) == 1: return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            for j in range(0, i-1):
                dp[i] = max(dp[i], nums[i] + dp[j])
        return(max(dp[-1], dp[-2]))
        '''
        dp = [0]*len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        return max(dp)