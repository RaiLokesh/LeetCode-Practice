from collections import defaultdict as dd
class Solution:
    def frequencySort(self, s: str) -> str:
        d = dd(lambda:0)
        for i in s: d[i]+=1
        def sorter(i):
            return d[i]
        s = [i for i in set(s)]
        s.sort(key=sorter, reverse=True)
        ans = ''
        for i in s: ans += i*d[i]
        return ans