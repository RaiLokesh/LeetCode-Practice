class Solution:
    ans = []
    def solve(i, neg, s):
        if i==0:
            if neg==0:
                Solution.ans.append(s)
            return
        Solution.solve(i-1, neg+1, s+'(')
        if neg:
            Solution.solve(i-1, neg-1, s+')')
    def generateParenthesis(self, n: int) -> List[str]:
        Solution.ans = []
        Solution.solve(2*n, 0, '')
        return Solution.ans