class Solution:
    ans = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = [i for i in range(1, n+1)]
        Solution.ans = []
        def solve(arr, i):
            if len(arr) == k:
                Solution.ans.append([i for i in arr])
            for i in range(i, len(l)):
                arr.append(l[i])
                solve(arr, i+1)
                arr.pop()
        solve([], 0)
        return Solution.ans