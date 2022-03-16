class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def solve(i, j):
            if i == len(t):
                return 1
            if j == len(s):
                return 0
            if t[i] == s[j]:
                return solve(i+1, j+1) + solve(i, j+1)
            else:
                return solve(i, j+1)
        return solve(0, 0)