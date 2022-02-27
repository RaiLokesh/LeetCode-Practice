from collections import defaultdict as dd

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = dd(lambda:0)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        #--- in 3x3 check for unique elements
                        if board[k][l] != ".":
                            d[board[k][l]] += 1
                            if d[board[k][l]] > 1: return False
                        #---
        #-- check for rows and cols
        for i in range(9):
            d1 = dd(lambda:0)
            d2 = dd(lambda:0)
            for j in range(9):
                if board[i][j] != ".":
                    d1[board[i][j]] += 1
                    if d1[board[i][j]] > 1: return False
                if board[j][i] != ".":
                    d2[board[j][i]] += 1
                    if d2[board[j][i]] > 1: return False
        return True