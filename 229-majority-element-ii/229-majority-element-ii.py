from collections import defaultdict as dd
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
         # -> aise 2 elements hi hai list mein
        ans = []
        d = dd(lambda:0)
        for i in nums:
            d[i] += 1
            if d[i] > len(nums)//3:
                ans.append(i)
                d[i] = -float('inf')
        return ans