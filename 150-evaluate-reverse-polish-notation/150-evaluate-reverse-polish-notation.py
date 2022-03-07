class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def ans(x, opr, y):
            if opr == '+': return int(x)+int(y)
            elif opr == '-': return int(x)-int(y)
            elif opr == '*': return int(x)*int(y)
            else:
                if (int(x) > 0 and int(y) > 0) or (int(x) < 0 and int(y) < 0):
                    return int(x)//int(y)
                else:
                    return (abs(int(x))//abs(int(y)))*-1
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                y = stack.pop()
                x = stack.pop()
                stack.append(ans(x, i, y))
            else:
                stack.append(i)
        return stack[-1]