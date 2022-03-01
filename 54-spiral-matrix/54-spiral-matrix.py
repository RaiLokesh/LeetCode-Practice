class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output, check = [], []
        m, n = len(matrix), len(matrix[0])
        def solve(i, j, last):
            if (i, j) in check or i==m or j==n or i==-1 or j==-1: return
            #print(i, j)
            output.append(matrix[i][j])
            check.append((i, j))
            if last == "right":
                if j+1 == n or (i, j+1) in check:
                    solve(i+1, j, "down")
                else:
                    solve(i, j+1, last)
            if last == "down":
                if i+1 == m or (i+1, j) in check:
                    solve(i, j-1, "left")
                else:
                    solve(i+1, j, "down")
            if last == "left":
                if j-1 == -1 or (i, j-1) in check:
                    solve(i-1, j, "up")
                else:
                    solve(i, j-1, "left")
            if last == "up":
                if i-1 == -1 or (i-1, j) in check:
                    solve(i, j+1, "right")
                else:
                    solve(i-1, j, "up")
        solve(0, 0, "right")
        return output