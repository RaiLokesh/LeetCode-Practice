from collections import defaultdict as dd
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = dd(lambda:0)
        d[nums[0]%k] += 1
        ans = 0
        if nums[0]%k==0: ans = 1
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i]%k==0: ans += 1
            if nums[i] % k < 0:
                if d[nums[i]%k + k]: ans += d[nums[i]%k + k]
                d[nums[i]%k + k] += 1
            else:
                if d[nums[i]%k]: ans += d[nums[i]%k]
                d[nums[i]%k] += 1
        return ans