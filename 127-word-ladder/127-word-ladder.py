from collections import deque as que
from string import ascii_lowercase as alphabets
class Solution:
    graph = {}
    ans = 0
    def traverse_graph(self, beginWord, endWord, pos):
        if beginWord == endWord:
            Solution.ans = pos
            return -1
        if beginWord not in Solution.graph: return 0
        for i in Solution.graph[beginWord]:
            if self.traverse_graph(i, endWord, pos + 1) == -1:
                return -1
        return 0
    
    def create_graph(self, beginWord, endWord, wordList):
        graph = {}
        q = que([beginWord])
        visited = {beginWord}
        while q:
            curr = q.popleft()
            for i in alphabets:
                temp = [j for j in curr]
                for j in range(len(curr)):
                    prev = temp[j]
                    temp[j] = i
                    st = ''.join(temp)
                    if st in wordList and st not in visited:
                        visited.add(st)
                        if curr not in graph: graph[curr] = []
                        graph[curr].append(st)
                        q.append(st)
                    temp[j] = prev
        Solution.graph = graph
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # -> reinitilize values for new objects
        Solution.graph = {}
        Solution.ans = 0
        wordList = set(wordList) #-> optimize
        # -> create graph
        self.create_graph(beginWord, endWord, wordList)
        # -> traverse graph
        self.traverse_graph(beginWord, endWord, 1)
        # -> return ans
        return Solution.ans