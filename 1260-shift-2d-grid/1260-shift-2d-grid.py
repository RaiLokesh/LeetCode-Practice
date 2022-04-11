class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ldr = []
        for i in grid:
            for j in i:
                ldr.append(j)
        n = len(ldr)
        k = k % n
        ldr = (ldr[n-k:]+ldr[:n-k])[::-1]
        for i in grid:
            for j in range(len(i)):
                i[j] = ldr.pop()
        return grid