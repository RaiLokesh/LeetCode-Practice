from collections import deque as que
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #if k==0: return 0
        q = que([])
        prod = 1
        i = 0
        ans = 0
        elemRemoved = 0
        while i < len(nums):
            prod *= nums[i]
            q.append(nums[i])
            while prod >= k:
                if not q: break
                prod //= q.popleft()
                elemRemoved += 1
            ans += i - elemRemoved + 1
            i += 1
        return ans