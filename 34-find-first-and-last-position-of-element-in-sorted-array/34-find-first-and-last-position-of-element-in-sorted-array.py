from bisect import bisect_left as bl, bisect_right as br
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if bl(nums, target)==len(nums) or nums[bl(nums, target)] != target:
            return [-1, -1]
        return [bl(nums, target), br(nums, target)-1]