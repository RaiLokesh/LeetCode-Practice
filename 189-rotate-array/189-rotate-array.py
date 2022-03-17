class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        arr = [i for i in nums]
        arr = (arr[:n-k][::-1] + arr[n-k:][::-1])[::-1]
        for i in range(n):
            nums[i] = arr[i]
            