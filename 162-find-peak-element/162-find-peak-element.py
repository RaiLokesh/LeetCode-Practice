class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]: return 0
        #if nums[len(nums)-1] > nums[len(nums)-2]: return len(nums)-1
        
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if mid > 0 and mid < len(nums)-1 and nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid - 1
        return i
        