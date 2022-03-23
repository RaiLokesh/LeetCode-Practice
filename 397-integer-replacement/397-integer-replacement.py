class Solution:
    def solve(self, n, count):
        if n == 1:
            return count
        if n%2:
            return min(self.solve(n-1, count+1), self.solve(n+1, count+1))
        else:
            return self.solve(n//2, count + 1)
    def integerReplacement(self, n: int) -> int:
        return self.solve(n, 0)