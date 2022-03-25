from collections import defaultdict as dd
class Solution:
    grid = []
    curr = 0
    def close_corner_dfs(self, i, j):
        Solution.grid[i][j] = 'X'
        if i+1 < len(Solution.grid) and Solution.grid[i+1][j] == 0:
            self.close_corner_dfs(i+1, j)
        if j+1 < len(Solution.grid[0]) and Solution.grid[i][j+1] == 0:
            self.close_corner_dfs(i, j+1)
        if i-1 >= 0 and Solution.grid[i-1][j] == 0:
            self.close_corner_dfs(i-1, j)
        if j-1 >= 0 and Solution.grid[i][j-1] == 0:
            self.close_corner_dfs(i, j-1)
    
    def dfs(self, i, j):
        Solution.grid[i][j] = Solution.curr
        if i+1 < len(Solution.grid) and Solution.grid[i+1][j] == 0:
            self.dfs(i+1, j)
        if j+1 < len(Solution.grid[0]) and Solution.grid[i][j+1] == 0:
            self.dfs(i, j+1)
        if i-1 >= 0 and Solution.grid[i-1][j] == 0:
            self.dfs(i-1, j)
        if j-1 >= 0 and Solution.grid[i][j-1] == 0:
            self.dfs(i, j-1)
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        Solution.grid = grid
        for i in range(len(grid)):
            if grid[i][0] == 0:
                self.close_corner_dfs(i, 0)
            if grid[i][-1] == 0:
                self.close_corner_dfs(i, len(grid[0])-1)
        
        for i in range(len(grid[0])):
            if grid[0][i] == 0:
                self.close_corner_dfs(0, i)
            if grid[-1][i] == 0:
                self.close_corner_dfs(len(grid)-1, i)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    Solution.curr -= 1
                    self.dfs(i, j)
                    
        d = dd(lambda:0)
        for i in grid:
            for j in i:
                if j != 'X' and j < 0: d[j]
        ans = 0
        for i in d: ans += 1
        return ans
                