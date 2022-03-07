from collections import deque as queue
class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # -> Check length condition for validity
        
        if len(s1) + len(s2) != len(s3): return False
        
        s1, s2 = s2, s1
        
        # -> make a (2m+1)x(2n+1) matrix
        
        m, n = len(s1), len(s2)
        matrix = [[0]*(2*n+1) for _ in range(2*m+1)]
        
        # -> fill alternate rows with s2 giving space in between
        
        count = 0
        for i in range(1, 2*m, 2):
            for j in range(0, 2*(n+1), 2):
                matrix[i][j] = s1[count]
            count += 1
        
        # -> fill alternate cols with s1 giving space in between
        
        for i in range(0, 2*(m+1), 2):
            count = 0
            for j in range(1, 2*n, 2):
                matrix[i][j] = s2[count]
                count += 1
        
        # -> perform bfs and try to reach (m-1, n-1) from (0, 0) 
        # -> if we can reach : ans is True else False
        
        visited = set()
        q = queue([(0, 0)])
        i = 0
        for i in s3:
            nn = len(q)
            for _ in range(nn):
                x = q.popleft()
                if x[0]+1 < 2*m+1 and matrix[x[0]+1][x[1]] == i:
                    if (x[0]+2, x[1]) not in visited:
                        q.append((x[0]+2, x[1]))
                        visited.add((x[0]+2, x[1]))
                if x[1]+1 < 2*n+1 and matrix[x[0]][x[1]+1] == i:
                    if (x[0], x[1]+2) not in visited:
                        q.append((x[0], x[1]+2))
                        visited.add((x[0], x[1]+2))
            if not q:
                return False
                break
        else: return True