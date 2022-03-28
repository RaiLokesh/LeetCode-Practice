class Solution:
    ans = []
    graph = []
    def solve(self, ptr, end, path):
        if ptr == end:
            Solution.ans.append(path)
            return
        for i in Solution.graph[ptr]:
            if i not in path:
                self.solve(i, end, path+[i])
                
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        Solution.ans = []
        Solution.graph = graph
        self.solve(0, len(graph)-1, [0])
        return Solution.ans