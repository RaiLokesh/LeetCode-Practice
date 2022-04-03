class Solution:
    @cache
    def solve(self, rem_sum_to_fulfill, mul):
        if rem_sum_to_fulfill == 0:
            return mul
        ans = 0
        for i in range(1, rem_sum_to_fulfill+1):
            ans = max(ans, self.solve(rem_sum_to_fulfill-i, mul*i))
        return ans
    
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        return self.solve(n, 1)