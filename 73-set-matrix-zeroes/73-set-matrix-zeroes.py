from collections import defaultdict as dd
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = dd(lambda:0), dd(lambda:0)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(m):
            for j in range(n):
                if row[i] or col[j] : matrix[i][j]=0
