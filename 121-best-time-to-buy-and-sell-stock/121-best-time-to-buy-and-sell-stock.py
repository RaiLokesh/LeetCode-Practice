class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mindiff = 0
        mini = max(prices)
        for i in prices:
            mini = min(mini, i)
            mindiff = max(mindiff, i-mini)
        return mindiff
        
        