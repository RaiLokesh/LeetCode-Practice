class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for j in range(len(rating)):
            temp1 = temp2 = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    temp1 += 1
                
            for k in range(j+1, len(rating)):
                if rating[k] > rating[j]:
                    temp2 += 1
                
            ans += temp1 * temp2
            temp1 = temp2 = 0
            for i in range(j):
                if rating[i] > rating[j]:
                    temp1 += 1
                
            for k in range(j+1, len(rating)):
                if rating[k] < rating[j]:
                    temp2 += 1
            ans += temp1*temp2
            
        return ans