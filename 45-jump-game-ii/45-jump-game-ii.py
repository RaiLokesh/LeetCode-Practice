from collections import defaultdict as dd
class Solution:
    d = dd(lambda:0)
    nums = []   # made nums global instead of passing in recursion
    n = 0
    def solve(i):
        if i>=Solution.n-1:
            return 0
        if i in Solution.d: return Solution.d[i]
        Solution.d[i] = 100000
        for j in range(1, Solution.nums[i]+1):
            Solution.d[i] = min(Solution.d[i], 1+Solution.solve(i+j))
        return Solution.d[i]
    def jump(self, nums: List[int]) -> int:
        Solution.d = {}
        Solution.nums = [i for i in nums]
        Solution.n = len(nums)
        ans = Solution.solve(0)
        return ans