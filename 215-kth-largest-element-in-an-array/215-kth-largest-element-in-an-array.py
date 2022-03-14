class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        for i in range(k):
            j = ~i
        return nums[j]