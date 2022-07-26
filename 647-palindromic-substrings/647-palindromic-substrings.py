class Solution:
    def countSubstrings(self, s: str) -> int:
        Solution.ans = 0
            
        def solve(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                Solution.ans += 1
                i -= 1
                j += 1
            
        for i in range(len(s)):
            Solution.ans += 1
            solve(i-1, i+1)
            solve(i, i+1)
            
        return Solution.ans