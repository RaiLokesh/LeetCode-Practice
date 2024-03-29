from collections import defaultdict as dd
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
		
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        
        edges.sort()
        
        roots = [i for i in range(len(points))]
        
        def find(v):
            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]
        
        def union(u, v):
            p1 = find(u); p2 = find(v)
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False
        
        res = 0
        for d, u, v in edges:
            if union(u, v):
                res += d
        return res