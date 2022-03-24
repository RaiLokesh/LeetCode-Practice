class Solution:
    ans = True
    visited = set()
    start = 0
    d = {}
    @cache
    def dfs(self, curr):
        if curr not in Solution.d: return
        for i in Solution.d[curr]:
            if i in Solution.visited:
                Solution.ans = False
                return
            else:
                Solution.visited.add(i)
                self.dfs(i)
                Solution.visited.remove(i)
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        for i in prerequisites:
            if i[::-1] in prerequisites: return False
        for i in prerequisites:
            if i[0] not in d:
                d[i[0]] = [i[1]]
            else:
                d[i[0]].append(i[1])
        Solution.visited = set()
        Solution.ans = True
        if len(prerequisites) == 0: return True
        Solution.d = d
        for i in prerequisites:
            Solution.visited = set()
            Solution.start = i[0]
            self.dfs(i[0])
            if Solution.ans == False: return False
        return Solution.ans
        