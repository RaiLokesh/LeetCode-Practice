from copy import deepcopy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if matrix[i][j]:
                    count = 0
                    if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1]:
                        count += 1
                    if i+1 < len(board) and j+1 < len(board[0]) and matrix[i+1][j+1]:
                        count += 1
                    if i-1 >= 0 and matrix[i-1][j]:
                        count += 1
                    if j-1 >= 0 and matrix[i][j-1]:
                        count += 1
                    if i+1 < len(matrix) and matrix[i+1][j]:
                        count += 1
                    if j+1 < len(matrix[0]) and matrix[i][j+1]:
                        count += 1
                    if i-1 >= 0 and j+1 < len(board[0]) and matrix[i-1][j+1]:
                        count += 1
                    if i+1 < len(board) and j-1 >=0 and matrix[i+1][j-1]:
                        count += 1
                    if count not in [2, 3]:
                        board[i][j] = 0
                else:
                    count = 0
                    if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1]:
                        count += 1
                    if i+1 < len(board) and j+1 < len(board[0]) and matrix[i+1][j+1]:
                        count += 1
                    if i-1 >= 0 and j+1 < len(board[0]) and matrix[i-1][j+1]:
                        count += 1
                    if i+1 < len(board) and j-1 >=0 and matrix[i+1][j-1]:
                        count += 1
                    if i-1 >= 0 and matrix[i-1][j]:
                        count += 1
                    if j-1 >= 0 and matrix[i][j-1]:
                        count += 1
                    if i+1 < len(matrix) and matrix[i+1][j]:
                        count += 1
                    if j+1 < len(matrix[0]) and matrix[i][j+1]:
                        
                        count += 1
                    if count == 3:
                        board[i][j] = 1
                    
                    