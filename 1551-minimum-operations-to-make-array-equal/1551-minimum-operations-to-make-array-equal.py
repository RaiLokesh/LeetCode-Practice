class Solution:
    def minOperations(self, n: int) -> int:
        flag = ans = 0
        if n % 2:
            flag = 2 * (n // 2) + 1
        else:
            flag = (2 * (n // 2) + 1 + 2 * (n // 2 - 1) + 1) // 2
        for i in range(n // 2):
            ans += flag - (2 * i + 1)
        return ans