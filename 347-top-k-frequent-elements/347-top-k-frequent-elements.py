from collections import defaultdict as dd
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dd(lambda:0)
        def dp(i):
            return i[-1]
        for i in nums: d[i] += 1
        l = sorted(d.items(), key=dp, reverse = True)
        ans = [0]*k
        for i in range(k):
            ans[i] = l[i][0]
        return ans