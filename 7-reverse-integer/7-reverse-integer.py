class Solution:
    def reverse(self, x: int) -> int:
        m = 2**31
        ans = 0
        if x < 0:
            x *= -1
            ans = (-1) * int(str(x)[::-1])
        else:
            ans = int(str(x)[::-1])
        if ans < (-1) * m or ans > m - 1:
            return 0
        return ans