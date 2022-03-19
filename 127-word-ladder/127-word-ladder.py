from collections import deque as que
from string import ascii_lowercase as alphabets
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # -> create graph like bfs using queues and visited sets
        
        q = que([beginWord])
        q_pos = que([1])
        wordList = set(wordList)  # -> only optimization needed
        while q:
            curr = q.popleft()
            curr_pos = q_pos.popleft()
            for i in alphabets:
                for j in range(len(curr)):
                    st = curr[:j] + i + curr[j+1:]
                    if st in wordList:
                        if st == endWord: return curr_pos+1
                        q.append(st)
                        q_pos.append(curr_pos+1)
                        wordList.remove(st)
        return 0
        
        