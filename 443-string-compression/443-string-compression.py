class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1: return 1
        l=[]
        count = 1
        for i in range(1, len(chars)):
            if chars[i]!=chars[i-1]:
                l.append(chars[i-1])
                if count>1:
                    for i in str(count):
                        l.append(i)
                count = 1
            else:
                count += 1
        if count:
            l.append(chars[-1])
            if count>1:
                for i in str(count):
                    l.append(i)
        n = len(l)
        for i in range(n):
            chars[i] = str(l[i])
        return n