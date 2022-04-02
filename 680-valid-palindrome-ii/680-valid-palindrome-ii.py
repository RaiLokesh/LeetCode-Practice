class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1] : return True
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return s[:i]+s[i+1:]==(s[:i]+s[i+1:])[::-1] or s[:j]+s[j+1:]==(s[:j]+s[j+1:])[::-1]
            i += 1
            j -= 1