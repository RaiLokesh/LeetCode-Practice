from collections import defaultdict as dd
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        array = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020]
        
        d = dd(lambda:0)
        ans = 0
        
        for i in time:
            ans += d[i]
            for j in array:
                if j >= i:
                    d[j-i] += 1
        return ans