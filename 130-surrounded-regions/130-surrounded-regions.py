class Solution:
    board = []
    visited = set()
    def fill_water(self, i, j):
        if (i, j) in Solution.visited: return
        Solution.visited.add((i, j))
        Solution.board[i][j] = "W"
        if i-1 >= 0 and Solution.board[i-1][j] == 'O': self.fill_water(i-1, j)
        if i+1 < len(Solution.board) and Solution.board[i+1][j] == 'O': self.fill_water(i+1, j)
        if j-1 >= 0 and Solution.board[i][j-1] == 'O': self.fill_water(i, j-1)
        if j+1 < len(Solution.board[0]) and Solution.board[i][j+1] == 'O': self.fill_water(i, j+1)
        
    def solve(self, board: List[List[str]]) -> None:
        Solution.board = board
        Solution.visited = set()
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.fill_water(0, i)
            if board[len(board)-1][i] == 'O':
                self.fill_water(len(board)-1, i)
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.fill_water(i, 0)
            if board[i][len(board[0])-1] == 'O':
                self.fill_water(i, len(board[0])-1)
        
        for i in range(len(Solution.board)):
            for j in range(len(Solution.board[0])):
                if Solution.board[i][j] == 'W':
                    Solution.board[i][j] = 'O'
                else:
                    Solution.board[i][j] = 'X'
        
        
        