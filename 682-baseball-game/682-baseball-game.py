class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append((2*int(stack[-1])))
            elif i == '+':
                stack.append((int(stack[-1]) + int(stack[-2])))
            else:
                stack.append(int(i))
        return sum(stack)