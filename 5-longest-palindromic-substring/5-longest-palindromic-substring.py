class Solution:
    def check_Palindrome(self, i, j, s, ans):
        while i>=0 and j<len(s) and s[i]==s[j] :
            ans = s[i:j+1]
            i-=1; j+=1
        return ans
            
    def longestPalindrome(self, s: str) -> str:
        # max of even length palindromes and odd length palindromes
        # for odd length send i-1, i+1
        # for even length send i, i+1
        ans = ''
        for i in range(len(s)):
            x = self.check_Palindrome(i-1, i+1, s, s[i])
            y = self.check_Palindrome(i, i+1, s, '')
            if len(x) > len(ans):
                ans = x
            if len(y) > len(ans):
                ans = y
        return ans