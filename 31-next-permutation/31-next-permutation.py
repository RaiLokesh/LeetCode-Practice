from bisect import bisect_right as bl
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #logic: start from end, find the first decreasing element; sort traversed elem, swap the first decreasing element with its immediate next successer in the sorted traversed elems.
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                x = nums[:i+1]
                y = sorted(nums[i+1:])
                t = x[-1]
                x[-1] = y[bl(y, x[-1])]
                y[bl(y, t)] = t
                ans = x + y
                for i in range(len(nums)): nums[i] = ans[i]
                return nums
        nums.sort()
        return nums
            
            
            