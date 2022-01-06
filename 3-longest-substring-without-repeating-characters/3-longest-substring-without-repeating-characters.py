from collections import defaultdict as dd
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dd(lambda:-1)
        start=0
        count=0
        ans=0
        for i in range(len(s)):
            if i<start: continue
            if d[s[i]]==-1 or (d[s[i]]!=-1 and d[s[i]]<start): 
                #print(s[i], start)
                count+=1
            else:
                #print(count, s[i])
                ans = max(ans, count)
                start = d[s[i]]+1
                count=i-start+1
            d[s[i]]=i
        count=len(s)-1-start+1
        ans = max(ans, count)
        return ans