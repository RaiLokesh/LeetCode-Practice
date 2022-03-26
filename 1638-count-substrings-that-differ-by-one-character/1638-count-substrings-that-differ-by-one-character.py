class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                temp = 0
                for k in range(len(t)):
                    
                    if i+k < len(s) and j+k < len(t) and s[i+k] != t[j+k]:
                        if temp: break
                        temp = 1
                    elif i+k < len(s) and j+k < len(t) and temp: temp += 1
                ans += temp
                    
        return ans