from collections import defaultdict as dd
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dd(lambda:[])
        def calculate(s):
            l = []
            for i in s:
                l.append(i)
            l.sort()
            return ''.join(l)
        for i in strs:
            d[calculate(i)].append(i)
        return list(d.values())