from collections import defaultdict as dd
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = dd(lambda:0)
        def solve(sm):
            if sm == 0:
                return 0
            if sm < 0:
                return float('inf')
            if d[sm]: return d[sm]
            mini = float('inf')
            for c in coins:
                if sm-c >= 0:
                    mini = min(mini, 1 + solve(sm-c))
            d[sm] = mini
            return mini
        ans = solve(amount)
        if ans == float('inf'): return -1
        return ans