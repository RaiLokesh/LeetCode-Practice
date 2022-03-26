class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*len(arr)
        dp[0] = arr[0]
        maxi = arr[0]
        for i in range(1, k):
            maxi = max(maxi, arr[i])
            dp[i] = maxi*(i+1)
            
        #print(dp)
        
        for i in range(k, len(arr)):
            count = 0
            for j in range(i-k+1, i+1):
                dp[i] = max(dp[i], dp[i-k+count] + max(arr[j:i+1])*len(arr[j:i+1]))
                count += 1
        
        return(dp[-1])