class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            x = sorted(nums[l[i]:r[i]+1])
            if len(x) in [1, 2]: ans.append(True); continue
            diff = x[1] - x[0]
            for j in range(1, len(x)):
                if x[j]-x[j-1] != diff:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans