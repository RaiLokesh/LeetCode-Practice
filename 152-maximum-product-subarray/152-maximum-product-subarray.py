class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = []
        l = []
        f_ans = nums[0]
        for i in nums:
            if i:
                temp.append(i)
            else:
                if temp: l.append(temp)
                temp = []
                f_ans = 0
        if temp: l.append(temp)
        if len(l) > 1: f_ans = 0
        for nums in l:
            left_prod = right_prod = 1
            ans = nums[0]
            for i in range(len(nums)):
                left_prod *= nums[i]
                right_prod *= nums[~i]
                ans = max(left_prod, right_prod, ans)
            f_ans = max(f_ans, ans)
        return f_ans