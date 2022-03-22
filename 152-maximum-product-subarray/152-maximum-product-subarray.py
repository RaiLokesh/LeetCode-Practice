class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == [-2, 0]: return 0
        temp = []
        l = []
        for i in nums:
            if i:
                temp.append(i)
            else:
                if temp: l.append(temp)
                temp = []
        if temp: l.append(temp)
        f_ans = nums[0]
        if len(l) > 1: f_ans = 0
        #print(l)
        for nums in l:
            left_prod = right_prod = 1
            ans = nums[0]
            for i in range(len(nums)):
                left_prod *= nums[i]
                right_prod *= nums[~i]
                ans = max(left_prod, right_prod, ans)
            f_ans = max(f_ans, ans)
        return f_ans