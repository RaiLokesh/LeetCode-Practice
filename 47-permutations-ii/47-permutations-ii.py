class Solution:
    f_ans = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        Solution.f_ans = []
        def solve(arr, ans):
            if not arr:
                if ans not in Solution.f_ans:
                    Solution.f_ans.append([i for i in ans])
                return
            for i in range(len(arr)):
                ans.append(arr[i])
                solve(arr[:i]+arr[i+1:], ans)
                ans.pop()
        solve(nums, [])
        return Solution.f_ans