from collections import defaultdict as dd
class Solution:
    def trap(self, height: List[int]) -> int:
        
        # -- calculate the right-max and left-max for each block
        
        d = dd(lambda:[0, 0])
        n = len(height)
        lmax = height[0]
        rmax = height[n-1]
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[n-i-1])
            d[i][0] = lmax
            d[n-i-1][-1] = rmax
        
        # -- for ans calculate the max water a block can hold above itself
        
        ans = 0
        for i in d:
            ans += min(d[i][0], d[i][-1]) - height[i]
        return ans