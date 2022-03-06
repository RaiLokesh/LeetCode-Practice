class Solution:
    ans = []
    def restoreIpAddresses(self, s: str) -> List[str]:
        Solution.ans = []
        def backtrack(l, i):
            if i == len(s):
                if len(l) == 4 and len(''.join(l))==len(s):
                    Solution.ans.append('.'.join(l))
                return
            t = ''
            if s[i] != '0':
                for j in range(i, len(s)):
                    if int(t+s[j]) < 256:
                        t += s[j]
                        backtrack(l+[t], j+1)
            else:
                backtrack(l+[s[i]], i+1)
        backtrack([], 0)
        return Solution.ans
                