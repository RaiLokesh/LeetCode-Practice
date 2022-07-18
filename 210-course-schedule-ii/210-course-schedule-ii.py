# -> topological sort
from collections import defaultdict as dd
class Solution:
    stack = []
    traversed = []
    graph = []
    graph = dd(lambda:[])
    def check(self, curr , visited):
        #print(dict(Solution.graph), curr)
        if curr in Solution.graph:
            for i in Solution.graph[curr]:
                if i in visited:
                    return True
                else:
                    visited.add(i)
                    if self.check(i, visited): return True
                    visited.remove(i)
        return False
    def checkCycle(self):
        visited = set()
        
        for i in Solution.graph:
            visited.add(i)
            if self.check(i, visited): return True
            visited.remove(i)
        return False
    def dfs(self, curr):
        for i in Solution.graph[curr]:
            if not Solution.traversed[i]:
                Solution.traversed[i] = True
                self.dfs(i)
                Solution.stack.append(i)
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        Solution.stack = []
        Solution.traversed = [False for i in range(numCourses)]
        Solution.graph = dd(lambda:[])
        for i in prerequisites:
            Solution.graph[i[1]].append(i[0])
        #print(dict(Solution.graph))
        if self.checkCycle(): return []
        for i in range(numCourses):
            if not Solution.traversed[i]:
                Solution.traversed[i] = True
                self.dfs(i)
                Solution.stack.append(i)
                #print(Solution.traversed, Solution.stack)
                
        return Solution.stack[::-1]