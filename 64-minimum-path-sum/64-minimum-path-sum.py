from collections import defaultdict as dd
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INT_MAX = 10**8
        m, n = len(grid), len(grid[0])
        d = dd(lambda:0)
        def solve(i, j):
            if i == m or j == n:
                return INT_MAX
            if i == m-1 and j == n-1:
                return grid[i][j]
            if d[(i, j)]: return d[(i, j)]
            d[(i, j)] = grid[i][j] + min(solve(i+1, j), solve(i, j+1))
            return d[(i, j)]
        return solve(0, 0)