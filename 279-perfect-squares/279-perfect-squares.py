from collections import defaultdict as dd

l = []
d = dd(lambda:0)
i = 1
while i**2 <= 10000:
    l.append(i**2)
    i += 1
def solve(sm):
    if sm == 0:
        return 1
    elif sm < 0: return 100000
    else:
        if d[sm]: return d[sm]
        ct = 100000
        for i in range(len(l)):
            ct = min(ct, 1 + solve(sm - l[i]))
        d[sm] = ct
        return ct

solve(10000)

class Solution:
    def numSquares(self, n: int) -> int:
        # -> run a loop to n and keep track of all i^2 values <= n
        # -> this problem is now transformed into coin problem (standard dp)
        return d[n]-1