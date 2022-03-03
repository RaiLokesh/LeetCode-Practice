from collections import defaultdict as dd
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [True] + [False] * len(s)
        d = dd(lambda:[])
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    if j==0:
                        d[i].append(s[j:i])
                    else:
                        temp = []
                        for k in d[j]:
                            d[i].append(k+" "+s[j:i])
        if dp[len(s)]:
            return d[len(s)]
        return []