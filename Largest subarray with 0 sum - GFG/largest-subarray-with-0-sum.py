#Your task is to complete this function
#Your should return the required output
from collections import defaultdict as dd
class Solution:
    def maxLen(self, n, arr):
        #Code here
        d = dd(lambda:-1)
        sm = maxi = 0
        for i in range(n):
            sm += arr[i]
            if d[sm] != -1:
                maxi = max(maxi, i-d[sm])
            else:
                d[sm] = i
            if sm==0:
                maxi = i+1
        return maxi 
        

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends