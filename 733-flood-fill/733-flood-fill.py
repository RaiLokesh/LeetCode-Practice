class Solution:
    newColor = 0
    oldColor = 0
    image = []
    visited = set()
    def fillColor(self, i, j):
        if (i, j) in Solution.visited: return
        Solution.visited.add((i, j))
        Solution.image[i][j] = Solution.newColor
        if i-1 >= 0 and Solution.image[i-1][j] == Solution.oldColor:
            self.fillColor(i-1, j)
        if j-1 >= 0 and Solution.image[i][j-1] == Solution.oldColor:
            self.fillColor(i, j-1)
        if i+1 < len(Solution.image) and Solution.image[i+1][j] == Solution.oldColor:
            self.fillColor(i+1, j)
        if j+1 < len(Solution.image[0]) and Solution.image[i][j+1] == Solution.oldColor:
            self.fillColor(i, j+1)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        Solution.oldColor = image[sr][sc]
        Solution.newColor = newColor
        Solution.image = image
        Solution.visited = set()
        self.fillColor(sr, sc)
        return Solution.image
        