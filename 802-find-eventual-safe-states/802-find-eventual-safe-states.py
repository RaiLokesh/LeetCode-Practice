class Solution:
    safeNodes, notSafeNodes = set(), set()
    graph = []
    def dfs(self, i, s):
        if i in Solution.safeNodes or Solution.graph[i] == []:
            Solution.safeNodes.add(i)
            return True
        if i in Solution.notSafeNodes:
            return False
        ans = True
        for j in Solution.graph[i]:
            if j in s:
                ans = False
                break
            ans = (ans and self.dfs(j, s.union(set([j]))))
        if ans:
            Solution.safeNodes.add(i)
        else: Solution.notSafeNodes.add(i)
        return ans
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        Solution.safeNodes, Solution.notSafeNodes = set(), set()
        Solution.graph = graph
        for i in range(len(graph)):
            self.dfs(i, set([i]))
        return sorted(Solution.safeNodes)
            