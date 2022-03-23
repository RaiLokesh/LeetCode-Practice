from itertools import permutations as pt
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def calculate(a, opr, b):
            if opr == "+":
                return int(a) + int(b)
            elif opr == "-":
                return int(a) - int(b)
            elif opr == "*":
                return int(a) * int(b)
            else:
                return "OPERATOR MISMATCH"
        
        exp = []
        t = ''
        indexes_of_oprs = []
        for i in range(len(expression)):
            if not expression[i].isdigit():
                exp.append(t)
                exp.append(expression[i])
                indexes_of_oprs.append(len(exp)-1)
                t = ""
            else: 
                t += expression[i]
        if t:
            exp.append(t)
        ans = []
        def solve(l):
            if len(l) == 1:
                return [l[0]]
            x = []
            for i in range(len(l)):
                if l[i] in ['+', '*', '-']:
                    val1 = solve(l[:i])
                    val2 = solve(l[i+1:])
                    temp = []
                    for j in val1:
                        for k in val2:
                            temp.append(calculate(j, l[i], k))
                    x += temp
            return x
        return solve(exp)