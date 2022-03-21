from collections import defaultdict as dd
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_flag = False
        row_flag = False
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_flag = True
                
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_flag = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        for i in range(len(matrix[0])):
            if row_flag:
                matrix[0][i] = 0
                
        for i in range(len(matrix)):
            if col_flag:
                matrix[i][0] = 0