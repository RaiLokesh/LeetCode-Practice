
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = [0]*(len(cost))
        d[0] = cost[0]
        d[1] = min(cost[1]+d[0], cost[1])
        for i in range(2, len(cost)):
            d[i] = cost[i] + min(d[i-1], d[i-2])
        #print(d)
        return min(d[-2], d[-1])