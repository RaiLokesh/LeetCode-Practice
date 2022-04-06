class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def solve(i, curr):
            if i >= len(prices):
                return 0
            ans = 0
            if curr != -1:
                
                for j in range(i, len(prices)):
                    if prices[j] > curr:
                        ans = max(ans, prices[j]-curr + solve(j+2, -1))
            else:
                for j in range(i, len(prices)):
                    ans = max(ans, solve(j+1, prices[j]))
            return ans
        return solve(0, -1)