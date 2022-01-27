class Solution:
    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        count = 0
        maxi = 0
        #print(satisfaction)
        for i in range(len(satisfaction)):
            count = 0
            k = 1
            for j in range(i, len(satisfaction)):
                count += (satisfaction[j]*k)
                k+=1
            maxi = max(maxi, count)
        return maxi