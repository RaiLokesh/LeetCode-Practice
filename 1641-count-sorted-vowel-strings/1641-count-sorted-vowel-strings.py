class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1 for i in range(5)]
        while True:
            if n==1: return sum(dp)
            for i in range(5):
                dp[i] = sum(dp[i:])
            n-=1
            