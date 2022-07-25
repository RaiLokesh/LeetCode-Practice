from collections import defaultdict as dd
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            if n: return [0]
            return []
        d = dd(lambda:set())
        for i in edges:
            d[i[0]].add(i[1])
            d[i[1]].add(i[0])
        small = []
        for i in d:
            if len(d[i]) <= 1: small.append(i)
        while len(d) > 2:
            #print(small)
            temp=[]
            for j in small:
                for i in d[j]:
                    d[i].remove(j)
                    if len(d[i]) <= 1: temp.append(i)
                del(d[j])
            small=[i for i in temp]
        return set(small)
            