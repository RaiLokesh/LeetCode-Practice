class Solution:
    prev = 9
    dp = [0]*9
    dp[0] = 1
    dp[1] = 10
    cnt = 9
    for i in range(2, 9):
        prev = prev * cnt
        dp[i] = prev + dp[i-1]
        cnt -= 1
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return Solution.dp[n]