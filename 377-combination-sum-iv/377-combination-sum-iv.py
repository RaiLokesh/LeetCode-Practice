class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def solve(sm):
            if sm >= target:
                if sm == target: return 1
                return 0
            ans = 0
            for i in nums:
                ans += solve(sm+i)
            return ans
        return solve(0)
        