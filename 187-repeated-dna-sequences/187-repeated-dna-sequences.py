from collections import defaultdict as dd

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return
        test_str = ''
        d = dd(lambda:0)
        for i in range(10):
            test_str += s[i]
        d[test_str] += 1
        for i in range(10, len(s)):
            test_str = test_str[1:] + s[i]  #this should give TLE due to slicing used
            d[test_str] += 1
        ans = []
        for i in d:
            if d[i] > 1:
                ans.append(i)
        return ans