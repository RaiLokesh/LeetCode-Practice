from collections import defaultdict as dd
class Solution:
    def numSplits(self, s: str) -> int:
        d1 = dd(lambda:0)
        d2 = dd(lambda:0)
        count1 = count2 = 0
        d1[s[0]] = 1
        count1 = 1
        for i in range(1, len(s)):
            if not d2[s[i]]: count2 += 1
            d2[s[i]] += 1
        #print(dict(d1), count1, dict(d2), count2)
        count = 0
        if count1 == count2: count = 1
        for i in range(1, len(s)-1):
            d2[s[i]] -= 1
            if d2[s[i]] == 0: count2 -= 1
            if not d1[s[i]]: count1 += 1
            d1[s[i]] += 1
            if count1 == count2: count += 1
        return count