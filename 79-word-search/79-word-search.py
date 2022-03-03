class Solution:
    ans = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        Solution.ans = False
        def solve(i, j, i_word, visited):
            #print(visited)
            if i_word == len(word):
                Solution.ans = True
                return
            if i+1 < m and (i+1, j) not in visited and word[i_word] == board[i+1][j]:
                visited.add((i+1, j))
                solve(i+1, j, i_word+1, visited)
                visited.remove((i+1, j))
            if j+1 < n and (i, j+1) not in visited and word[i_word] == board[i][j+1]:
                visited.add((i, j+1))
                solve(i, j+1, i_word+1, visited)
                visited.remove((i, j+1))
            if i-1 > -1 and (i-1, j) not in visited and word[i_word] == board[i-1][j]:
                
                visited.add((i-1, j))
                solve(i-1, j, i_word+1, visited)
                visited.remove((i-1, j))
            if j-1 > -1 and (i, j-1) not in visited and word[i_word] == board[i][j-1]:
                #print("HELLLO")
                visited.add((i, j-1))
                solve(i, j-1, i_word+1, visited)
                visited.remove((i, j-1))
        for i in range(m):
            if Solution.ans: return Solution.ans
            for j in range(n):
                if Solution.ans: return Solution.ans
                if board[i][j] == word[0]:
                    solve(i, j, 1, {(i, j)})
        return Solution.ans