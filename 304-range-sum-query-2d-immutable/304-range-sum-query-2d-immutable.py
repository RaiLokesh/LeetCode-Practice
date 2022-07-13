class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = matrix
        self.setPrefixSum()
    
    def setPrefixSum(self):
        row = [0] * len(self.prefixSum[0])
        self.prefixSum = [row] + self.prefixSum
            
        for i in range(len(self.prefixSum)):
            self.prefixSum[i] = [0] + self.prefixSum[i]
        
        for i in range(1, len(self.prefixSum)):
            for j in range(1, len(self.prefixSum[0])):
                self.prefixSum[i][j] += self.prefixSum[i][j-1] + self.prefixSum[i-1][j] - self.prefixSum[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2+1][col2+1] - self.prefixSum[row1][col2+1] - self.prefixSum[row2+1][col1] + self.prefixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)