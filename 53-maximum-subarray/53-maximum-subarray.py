class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        sm = 0
        ans = nums[0]
        for i in range(len(nums)):
            sm = max(sm+nums[i], nums[i])
            ans = max(ans, sm)
        return ans