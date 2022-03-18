class Solution:
    d = {}
    def palindrome(self, s):
        return s == s[::-1]
    
    def solve(self, s):
        if s == "":
            return 0
        if s in Solution.d: return Solution.d[s]
        mincount = float('inf')
        count = 0
        for i in range(1, len(s)+1):
            if self.palindrome(s[:i]):
                count = 1 + self.solve(s[i:])
                mincount = min(count, mincount)
        Solution.d[s] = mincount
        return mincount
    
    def minCut(self, s: str) -> int:
        return self.solve(s)-1