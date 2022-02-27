from collections import defaultdict as dd
class Solution:
    d = dd(lambda:0)
    n = 0
    ans = []
    def solve(i, curr_arr):
        if i == Solution.n:
            temp = [i for i in curr_arr]
            Solution.ans.append(temp)
            return
        for k in Solution.d:
            if Solution.d[k]:
                Solution.d[k]-=1
                curr_arr[i] = k
                Solution.solve(i+1, curr_arr)
                curr_arr[i] = 0
                Solution.d[k]+=1
    def permute(self, nums: List[int]) -> List[List[int]]:
        Solution.d = dd(lambda:0)
        Solution.n = len(nums)
        Solution.ans = []
        curr_arr = [0]*Solution.n
        for i in nums:
            Solution.d[i] += 1
        Solution.solve(0, curr_arr)
        return Solution.ans