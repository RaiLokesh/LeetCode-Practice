class Solution:
    #visited = set()
    grid = []
    counter = 1
    def groupIslands(self, i, j):
        #if (i, j) in Solution.visited: return
        #Solution.visited.add((i, j))
        Solution.grid[i][j] = str(Solution.counter)
        if i-1 >= 0 and Solution.grid[i-1][j] == '1': self.groupIslands(i-1, j)
        if j-1 >= 0 and Solution.grid[i][j-1] == '1': self.groupIslands(i, j-1)
        if i+1 < len(Solution.grid) and Solution.grid[i+1][j] == '1': self.groupIslands(i+1, j)
        if j+1 < len(Solution.grid[0]) and Solution.grid[i][j+1] == '1': self.groupIslands(i, j+1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        #Solution.visited = set()
        Solution.grid = grid
        Solution.counter = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    Solution.counter += 1
                    self.groupIslands(i, j)
        
        ans = set()
        for i in grid:
            for j in i:
                ans.add(j)
                
        if '0' in ans: return len(ans)-1
        return len(ans)