class Solution:
    grid = []
    
    @cache
    def dfs(self, i, j):
        Solution.grid[i][j] = 0
        if i+1 < len(Solution.grid) and Solution.grid[i+1][j] == 1:
            self.dfs(i+1, j)
        if j+1 < len(Solution.grid[0]) and Solution.grid[i][j+1] == 1:
            self.dfs(i, j+1)
        if i-1 >= 0 and Solution.grid[i-1][j] == 1:
            self.dfs(i-1, j)
        if j-1 >= 0 and Solution.grid[i][j-1] == 1:
            self.dfs(i, j-1)
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        Solution.grid = grid
        
        for i in range(len(grid)):
            if grid[i][0] == 1:
                self.dfs(i, 0)
            if grid[i][len(grid[0])-1] == 1:
                self.dfs(i, len(grid[0])-1)
        
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                self.dfs(0, i)
            if grid[len(grid)-1][i] == 1:
                self.dfs(len(grid)-1, i)
        
        ans = 0
        for i in grid:
            ans += i.count(1)
        return ans