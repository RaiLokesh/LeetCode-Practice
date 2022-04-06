import copy
from collections import defaultdict as dd
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        d = dd(lambda:0)
        for k in range( len(arr)):
            d[arr[k]]+=1
        for i in range(len(arr)):
            d[arr[i]] -= 1
            d1 = copy.deepcopy(d)
            for j in range(i+1, len(arr)):
                k = target - arr[i] - arr[j]
                d1[arr[j]] -= 1
                ans += d1[k]
                ans %= (10**9)+7
        return ans