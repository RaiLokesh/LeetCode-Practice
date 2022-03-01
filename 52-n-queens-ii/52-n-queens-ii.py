from collections import defaultdict as dd
class Solution:
    digonal1 = dd(lambda:0)
    digonal2 = dd(lambda:0)
    count = 0
    def totalNQueens(self, n: int) -> List[List[str]]:
        arr = []
        for i in range(n):
            arr.append("."*n)
        Solution.count = []
        Solution.digonal1 = dd(lambda:0)
        Solution.digonal2 = dd(lambda:0)
        def solve_Queens(curr_row, visited_cols, ans):
            if curr_row==n:
                x = [i for i in ans]
                Solution.count.append(x)
                return
            for col in range(n):
                if col in visited_cols or Solution.digonal1[col-curr_row] or Solution.digonal2[col+curr_row]:
                    continue
                visited_cols.append(col)
                Solution.digonal1[col-curr_row] = 1
                Solution.digonal2[col+curr_row] = 1
                t = ['.']*n
                t[visited_cols[-1]] = 'Q'
                t = ''.join(t)
                ans.append(t)
                solve_Queens(curr_row+1, visited_cols, ans)
                ans.pop()
                visited_cols.pop()
                Solution.digonal1[col-curr_row] = 0
                Solution.digonal2[col+curr_row] = 0
        solve_Queens(0, [], [])
        return len(Solution.count)