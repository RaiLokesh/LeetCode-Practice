class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        x = ['' for i in range(numRows)]
        i = 0
        j =0
        m=-1
        while i<len(s):
            if not j%(numRows-1): m*=-1
            x[j] += s[i]
            j+=m
            i+=1
        return (''.join(x))