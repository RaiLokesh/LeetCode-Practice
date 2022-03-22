class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        mini = nums[0]
        while i < j:
            mid = (i + j)//2
            mini = min(nums[i], nums[j], nums[mid], mini)
            if nums[mid] < nums[i] and nums[mid] < nums[j]:
                j = mid -1
            elif nums[mid] > nums[i] and nums[mid] > nums[j]:
                i = mid + 1
            else: # sorted case cover hojyega neeche wale statement mein toh chhod rha
                break
        return mini