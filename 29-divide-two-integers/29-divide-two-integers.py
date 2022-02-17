class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mins = False
        if dividend < 0:
            dividend *= -1
            mins = not mins
        if divisor < 0:
            divisor *= -1
            mins = not mins
        quotient = dividend // divisor
        if mins: quotient *= -1
        if quotient > (2**31 - 1):
            return 2**31 - 1
        elif quotient < -(2**31):
            return -(2**31)
        else:
            return quotient