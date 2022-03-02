class Solution:
    ans = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Solution.ans = []
        def solve(l, i):
            if i == len(nums):
                Solution.ans.append(l)
                return
            solve(l, i+1)
            solve(l + [nums[i]], i+1)
        solve([], 0)
        return Solution.ans