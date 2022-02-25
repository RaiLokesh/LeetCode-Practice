from collections import defaultdict as dd
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = dd(lambda:'')
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        ans = []
        for i in digits:
            l = len(ans)
            s = d[i]
            for j in s:
                if l:
                    for k in range(l):
                        ans.append(ans[k]+j)
                else:
                    ans.append(j)
            ans = ans[l:]
        return ans