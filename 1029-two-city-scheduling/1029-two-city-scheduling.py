class Solution:
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def sortcrow(a):
            return a[1] - a[0]
        costs.sort(key = sortcrow)
        ans = 0
        for i in range(len(costs)//2):
            ans += costs[i][1] + costs[len(costs)//2+i][0]
        return ans