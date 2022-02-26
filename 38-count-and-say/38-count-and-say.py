from collections import defaultdict as dd
class Solution:
    def countAndSay(self, n: int) -> str:
        stri = '1'
        for i in range(2, n+1):
            arr = ''
            count = 1
            for j in range(1, len(stri)):
                if stri[j] != stri[j-1]:
                    arr += str(count)+stri[j-1]
                    count = 1
                else:
                    count += 1
            if count:
                arr = arr + str(count) + stri[-1]
            stri = arr
        return stri