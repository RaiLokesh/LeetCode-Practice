class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        init = 0
        l = [0 for i in range(n+1)]
        if n == 0: return l
        l[1] = 1
        for i in range(2, n+1):
            if 2**(count+1) == i:
                count += 1
            xc = 2**count
            l[i] = 1 + l[i-xc]
            
        return l