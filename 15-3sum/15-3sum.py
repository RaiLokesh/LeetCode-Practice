from collections import defaultdict as dd
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output =[]
        n = len(nums)
        for i in range(n):
            lb = i+1
            ub = n-1
            while lb < ub:
                if nums[i] + nums[lb] + nums[ub] == 0:
                    output.append([nums[i], nums[lb], nums[ub]])
                    lb += 1
                    ub -= 1
                elif nums[i] + nums[lb] + nums[ub] < 0:
                    lb += 1
                else:
                    ub -= 1
        output.sort()
        if output==[]: return []
        out = [output[0]]
        for i in range(1 , len(output)):
            if output[i] != output[i-1]: out.append(output[i])
        return out
            