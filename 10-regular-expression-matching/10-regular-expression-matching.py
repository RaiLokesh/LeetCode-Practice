class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def solve(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p): return False
            
            if j < len(p)-1  and p[j+1] == "*":
                if i < len(s) and (p[j] == "." or s[i] == p[j]):
                    return solve(i+1, j) or solve(i, j+2) or solve(i+1, j+2)
                else:
                    return solve(i, j+2)
            
            else:
                if i < len(s) and (p[j] == "." or s[i] == p[j]):
                    return solve(i+1, j+1)
                else: return False
            
        
        return solve(0, 0)