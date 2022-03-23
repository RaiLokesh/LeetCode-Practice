class Solution:
    def divide(self, dividend, divisor):
        return str(dividend // divisor)
    def multiply(self, multiplicand, multiplier):
        return str(multiplicand * multiplier)
    def add(self, operand1, operand2):
        return str(operand1 + operand2)
    def substract(self, operand1, operand2):
        return str(operand1 - operand2)
        
    def calculate(self, s: str) -> int:
        temp = ''
        s1 = []
        for i in s:
            if i == ' ': continue
            if i in '+-*/':
                s1.append(temp)
                s1.append(i)
                temp = ''
            else: temp += i
        if temp:
            s1.append(temp)
        
        # -> divide or multiply
        s = [i for i in s1]
        s1 = []
        i = 0
        while i < len(s):
            if s[i] == '/':
                s1.append(self.divide(int(s1.pop()), int(s[i+1])))
                i += 1
            elif s[i] == '*':
                s1.append(self.multiply(int(s1.pop()), int(s[i+1])))
                i += 1
            else:
                s1.append(s[i])
            i += 1
        
        
        # -> add or substract
        s = [i for i in s1]
        s1 = []
        i = 0
        while i < len(s):
            if s[i] == '+':
                s1.append(self.add(int(s1.pop()), int(s[i+1])))
                i += 1
            elif s[i] == '-':
                s1.append(self.substract(int(s1.pop()), int(s[i+1])))
                i += 1
            else:
                s1.append(s[i])
            i += 1
            
        
        return (s1[0])
            
        