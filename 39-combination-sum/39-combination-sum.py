
class Solution:
    ans = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        Solution.ans = []
        def solve(arr):
            if sum(arr) == target:
                x = sorted([i for i in arr])
                if x not in Solution.ans:
                    Solution.ans.append(x)
                return
            if sum(arr) > target:
                return
            for j in range(len(candidates)):
                arr.append(candidates[j])
                solve(arr)
                arr.pop()
        solve([])
        return Solution.ans