class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sorter(a):
            x1, y1 = a
            return (x1**2 + y1**2)
        
        points.sort(key=sorter)
        
        return points[:k]