from collections import defaultdict as dd
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums[0] = nums[0]%k
        ans = False
        d = dd(lambda:100001)
        d[nums[0]] = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            nums[i] = nums[i]%k
            if nums[i] == 0 and i >= 1:
                ans = True
            if d[nums[i]] != 100001:
                if i - d[nums[i]] > 1:
                    ans = True
            else: d[nums[i]] = i
        return ans