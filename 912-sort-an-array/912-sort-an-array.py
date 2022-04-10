class Solution:
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        x = self.mergeSort(nums[len(nums)//2:])
        y = self.mergeSort(nums[:len(nums)//2])
        ans = []
        i = j = 0
        while i < len(x) or j < len(y):
            if i < len(x) and j < len(y):
                if x[i] < y[j]:
                    ans.append(x[i])
                    i += 1
                else:
                    ans.append(y[j])
                    j += 1
            elif i < len(x):
                ans.append(x[i])
                i += 1
            elif j < len(y):
                ans.append(y[j])
                j += 1
        return ans
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)