from collections import defaultdict as dd
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = [dd(lambda:0) for i in range(len(nums))]
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                d[i][nums[j]-nums[i]] = d[j][nums[j]-nums[i]] + 1
        for i in d:
            ans = max(ans, max(i.values()))
        
        return ans+1