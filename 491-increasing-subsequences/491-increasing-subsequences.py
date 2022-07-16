class Solution:
    ans = set()
    def solve(self, curr, nums):
        #print(curr, nums)
        for i in range(len(nums)):
            if not curr: self.solve((nums[i],), nums[i+1:])
            else:
                if nums[i] >= (curr[-1]):
                    self.solve(curr+(nums[i],), nums[i+1:])
                    Solution.ans.add(curr+(nums[i],))
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        Solution.ans = set()
        self.solve(tuple(), nums)
        return Solution.ans