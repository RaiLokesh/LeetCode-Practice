class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        maxi = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maxi = max(maxi, dp[i][0])
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            maxi = max(maxi, dp[0][i])
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxi = max(maxi, dp[i][j])
        return maxi**2
            