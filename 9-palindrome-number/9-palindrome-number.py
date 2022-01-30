class Solution:
    def isPalindrome(self, x: int) -> bool:
        neg = False
        if x<0:
            x*=-1
            neg = True
        n = x
        y = 0
        p = 1
        while n!=0:
            t = n%10
            n//=10
            y=y*10+t
        if neg: y*=-1
        return x==y