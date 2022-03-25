from collections import defaultdict as dd
class Solution:
    curr = 1
    graph = []
    def dfs(self, i, j):
        Solution.graph[i][j] = Solution.curr
        if i+1 < len(Solution.graph) and Solution.graph[i+1][j] == 1: self.dfs(i+1, j)
        if j+1 < len(Solution.graph[0]) and Solution.graph[i][j+1] == 1: self.dfs(i, j+1)
        if i-1 >= 0 and Solution.graph[i-1][j] == 1: self.dfs(i-1, j)
        if j-1 >= 0 and Solution.graph[i][j-1] == 1: self.dfs(i, j-1)
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Solution.graph = grid
        Solution.curr = 1
        maxi = 0
        d = dd(lambda:0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    Solution.curr += 1
                    self.dfs(i, j)
        
        for i in grid:
            for j in i:
                if j != 0:
                    d[j] += 1
                    maxi = max(maxi, d[j])
        return maxi