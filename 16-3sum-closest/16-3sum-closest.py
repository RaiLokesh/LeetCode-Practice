from collections import defaultdict as dd
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        #print(nums)
        mini = 10000000000
        ans=[]
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            sm = target - nums[i]
            
            while j<k:
                
                t=[]
                t.append(nums[i])
                t.append(nums[j])
                t.append(nums[k])
                ans.append(t)
                t=[]
                if nums[i]+nums[j]+nums[k]>target:
                    k-=1
                else:
                    j+=1
                
            
        #print(ans)
        ret = 0
        for i in range(len(ans)):
            ans[i] = sum(ans[i])
            t = ans[i]
            ans[i] = abs(target-ans[i])
            if ans[i]<mini:
                mini = ans[i]
                ret = t
            
        return ret