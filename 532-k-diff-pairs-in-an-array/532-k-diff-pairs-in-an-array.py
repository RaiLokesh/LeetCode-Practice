from collections import defaultdict as dd
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = dd(lambda:set())
        ans = set()
        for i in range(len(nums)):
            d[nums[i]].add(i)
        for i in range(len(nums)):
            if d[nums[i]+k]:
                for j in d[nums[i]+k]:
                    if i != j:
                        ans.add((max(nums[i], nums[j]), min(nums[i], nums[j])))

        return len(ans)