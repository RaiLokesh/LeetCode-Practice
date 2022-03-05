class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        index = [1, 0]
        d = {0:[nums[0]]}
        for i in range(1, len(nums)):
            l = []
            for j in range(i-1, -1 , -1):
                if nums[i] % nums[j] == 0 and dp[j]+1>dp[i]:
                    dp[i] = dp[j] + 1
                    l = [i for i in d[j]]
                    if dp[i] > index[0]:
                        index[0] = dp[i]
                        index[1] = i
            l.append(nums[i])
            d[i] = l
        return d[index[1]]