from collections import defaultdict as dd
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        array = [0, 60]
        time = [i%60 for i in time]
        d = dd(lambda:0)
        ans = 0
        for i in time:
            ans += d[i]
            for j in array:
                if j >= i:
                    d[j-i] += 1
        return ans