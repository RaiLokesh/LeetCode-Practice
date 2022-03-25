from collections import defaultdict as dd
class Solution:
    visited = {}
    grid2 = []
    curr = 1
    @cache
    def dfs(self, i, j):
        Solution.visited.add((i, j))
        if i+1 < len(Solution.grid2) and Solution.grid2[i+1][j] == 1 and (i+1, j) not in Solution.visited:
            self.dfs(i+1, j)
        if j+1 < len(Solution.grid2[0]) and Solution.grid2[i][j+1] == 1 and (i, j+1) not in Solution.visited:
            self.dfs(i, j+1)
        if i-1 >= 0 and Solution.grid2[i-1][j] == 1 and (i-1, j) not in Solution.visited:
            self.dfs(i-1, j)
        if j-1 >= 0 and Solution.grid2[i][j-1] == 1 and (i, j-1) not in Solution.visited:
            self.dfs(i, j-1)
    @cache
    def f_dfs(self, i, j):
        Solution.grid2[i][j] = Solution.curr
        if i+1 < len(Solution.grid2) and Solution.grid2[i+1][j] == 'T':
            self.f_dfs(i+1, j)
        if j+1 < len(Solution.grid2[0]) and Solution.grid2[i][j+1] == 'T':
            self.f_dfs(i, j+1)
        if i-1 >= 0 and Solution.grid2[i-1][j] == 'T':
            self.f_dfs(i-1, j)
        if j-1 >= 0 and Solution.grid2[i][j-1] == 'T':
            self.f_dfs(i, j-1)
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        Solution.grid2 = grid2
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    Solution.visited = set()
                    self.dfs(i, j)
                    for k in Solution.visited:
                        if not grid1[k[0]][k[1]]:
                            break
                    else:
                        for k in Solution.visited:
                            grid2[k[0]][k[1]] = 'T'
                            
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 'T':
                    Solution.curr += 1
                    self.f_dfs(i, j)
                    
        d = dd(lambda:0)
        for i in grid2:
            for j in i: d[j] = 1
        k = list(d.keys())
        return len(k)-k.count(0)-k.count(1)
            