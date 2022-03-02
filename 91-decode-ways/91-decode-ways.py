class Solution:
    ans = 0
    def numDecodings(self, s: str) -> int:
        def check_4_valid_2_digit_no(s):
            if s[0] == "0" or int(s) > 26:
                return False
            return True
        n = len(s)
        Solution.ans = 0
        dp = {}
        def solve(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]
            x = solve(i+1)
            if i+1 < n and check_4_valid_2_digit_no(s[i]+s[i+1]):
                x += solve(i+2)
            dp[i] = x
            return x
        return solve(0)