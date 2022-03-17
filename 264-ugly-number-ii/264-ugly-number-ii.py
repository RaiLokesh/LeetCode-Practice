class Solution:
    final = {1, 2, 3, 4, 5}
    curr = {3, 4, 5}
    while len(final) < 5000: # took a relatively large no. to accomodate the lesser values to be found later (ex. case for n = 1690)
        temp = set()
        for i in curr:
            temp.add(i*2)
            temp.add(i*3)
            temp.add(i*5)
        final.update(temp)
        curr = temp
    final = sorted(list(final))
    
    def nthUglyNumber(self, n: int) -> int:
        return Solution.final[n-1]