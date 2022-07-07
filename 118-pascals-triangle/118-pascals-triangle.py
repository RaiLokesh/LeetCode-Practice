class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        stack = [[1]]
        for i in range(2, numRows+1):
            temp = []
            for j in range(len(stack[-1])+1):
                if j == 0:
                    temp.append(stack[-1][j]+0)
                elif j == len(stack[-1]):
                    temp.append(stack[-1][j-1]+0)
                else:
                    temp.append(stack[-1][j] + stack[-1][j-1])
            stack.append(temp)
        return stack