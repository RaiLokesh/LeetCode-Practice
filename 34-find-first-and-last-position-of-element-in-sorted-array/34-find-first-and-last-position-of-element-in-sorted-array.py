from bisect import bisect_left as bl, bisect_right as br
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [bl(nums, target), br(nums, target)-1]
        
        if ans[0] == len(nums) or nums[ans[0]] != target:
            return [-1, -1]
        
        return ans