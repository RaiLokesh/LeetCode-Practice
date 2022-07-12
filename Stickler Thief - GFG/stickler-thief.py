class Solution:  
    
    #Function to find the maximum money the thief can get.4
    
    def FindMaxSum(self,a, n):
        dp = [0]*n
        if len(a) == 0: return 0
        if len(a) == 1: return a[0]
        dp[0], dp[1] = a[0], max(a[0], a[1])
        for i in range(2, n):
            dp[i] = max(a[i]+dp[i-2], dp[i-1])
            
        return dp[n-1]
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends