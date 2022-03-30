from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        for i in range(1, len(matrix)):
            matrix[0] += matrix[i]
        heapify(matrix[0])
        ans = 0
        while k:
            ans = heappop(matrix[0])
            k -= 1
        return ans