from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * (-1)
        
        heapify(stones)
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            val = abs(abs(x)-abs(y))
            if val:
                heappush(stones, val*(-1))
        if stones:
            return heappop(stones) * (-1)
        return 0