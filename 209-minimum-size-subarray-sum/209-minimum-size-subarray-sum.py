from collections import deque as que
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums): return 0
        q = que([])
        sm = 0
        ans = len(nums)
        for i in range(len(nums)):
            sm += nums[i]
            q.append(nums[i])
            if sm >= target:
                while sm - q[0] >= target:
                    sm -= q.popleft()
                ans = min(ans, len(q))
        return ans
            