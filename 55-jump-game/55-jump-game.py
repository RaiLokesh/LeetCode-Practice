class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums)>1: return False
        elif 0 not in nums or (0 in nums and len(nums)==1): return True
        else:
            max_index = nums[0]
            for i in range(1, len(nums)):
                if max_index >= len(nums)-1:
                    return True
                if nums[i] == 0:
                    if max_index <= i:
                        return False
                else:
                    max_index = max(max_index, i+nums[i])
            return False