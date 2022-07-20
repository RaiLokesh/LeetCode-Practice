from collections import defaultdict as dd
class Solution:
    visited = set()
    d = dd(lambda:set())
    def dfs(self, ptr):
        for i in Solution.d[ptr]:
            if i not in Solution.visited:
                Solution.visited.add(i)
                self.dfs(i)
    
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        riches = dd(lambda:set())
        for i in richer:
            riches[i[1]].add(i[0])
        answer = [0]*len(quiet)
        Solution.d = riches
        for i in range(len(answer)):
            Solution.visited = set()
            Solution.visited.add(i)
            self.dfs(i)
            mini = [-1, -1]
            for j in Solution.visited:
                if mini == [-1, -1]:
                    mini = [quiet[j], j]
                else:
                    if quiet[j] < mini[0]:
                        mini = [quiet[j], j]
            answer[i] = mini[1]
        return answer