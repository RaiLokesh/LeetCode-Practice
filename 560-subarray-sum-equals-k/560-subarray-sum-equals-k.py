from collections import defaultdict as dd
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dd(lambda:0)
        d[nums[0]] = 1
        ans = 0
        if nums[0]==k: ans+=1
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i]==k: ans += 1
            if d[nums[i]-k]: ans += d[nums[i]-k]
            d[nums[i]] += 1
            #print(nums[i], dict(d), ans)
        return ans