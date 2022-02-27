class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip().split()
        if not s: return 0
        neg = False
        if s[0][0] == "+":
            neg = False
            s[0] = s[0][1:]
            
        elif s[0][0] == '-':
            neg = True
            s[0] = s[0][1:]
        st = ''
        if not s: return 0
        for i in s[0]:
            if i.isdigit():
                st+=i
            else: break
        if st == "": return 0
        st = int(st)
        if neg:
            st *= -1
            if st < (2**31)*-1:
                return (2**31)*-1
            return st
        else:
            if st > (2**31)-1:
                return (2**31)-1
            return st