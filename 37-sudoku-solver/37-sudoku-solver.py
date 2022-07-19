from collections import defaultdict as dd
class Solution:
    
    def squareNumber(self, m, n):
        count = 0
        for i in range(3, 10, 3):
            for j in range(3, 10, 3):
                if m < i and n < j:
                    return count
                count += 1
    
    def solve(self, board, dRow, dCol, dSqrs):
        #print(dict(dRow))
        foundAns = True
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    foundAns = False
                    #- > write logic here
                    for k in range(1, 10):
                        if str(k) not in dRow[i] and str(k) not in dCol[j] and str(k) not in dSqrs[self.squareNumber(i, j)]:
                            board[i][j] = str(k)
                            dRow[i].add(str(k))
                            dCol[j].add(str(k))
                            dSqrs[self.squareNumber(i, j)].add(str(k))
                            check = self.solve(board, dRow, dCol, dSqrs)
                            if check:
                                return check
                            else:
                                board[i][j] = '.'
                                dRow[i].remove(str(k))
                                dCol[j].remove(str(k))
                                dSqrs[self.squareNumber(i, j)].remove(str(k))
                    return []
                    
        if foundAns: return board
        else: return []
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dRow = dd(lambda:set())
        dCol = dd(lambda:set())
        dSqrs = dd(lambda:set())
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                dRow[i].add(board[i][j])
                dCol[j].add(board[i][j])
                dSqrs[self.squareNumber(i, j)].add(board[i][j])
        #print(dict(dRow))
        #print(dict(dCol))
        #print(dict(dSqrs))
        return self.solve(board, dRow, dCol, dSqrs)