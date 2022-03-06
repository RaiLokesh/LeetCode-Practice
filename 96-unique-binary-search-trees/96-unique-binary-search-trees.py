from collections import defaultdict as dd
class Solution:
    def numTrees(self, n: int) -> int:
        d = dd(lambda:0)
        def solve(i, j):
            if i==j:
                return 1
            lvl_sum = 0
            if d[(i, j)]: return d[(i, j)]
            for k in range(i, j+1):
                l = max(1, solve(i, k-1))
                r = max(1, solve(k+1, j))
                lvl_sum += l*r
            d[(i, j)] = lvl_sum
            return lvl_sum
        return solve(0, n-1)