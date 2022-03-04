class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        if s=="" and t=="": return True
        if not t: return False
        while i < len(s):
            if t[j] == s[i]:
                i += 1
            j += 1
            if j == len(t) and i != len(s):
                return False
                break
        else:
            return True