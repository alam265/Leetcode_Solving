
'''Naive Approach'''
matrix = [[3, 0, 1, 4, 2], 
          [5, 6, 3, 2, 1], 
          [1, 2, 0, 1, 5], 
          [4, 1, 0, 1, 7], 
          [1, 0, 3, 0, 5]]

def sumRegion(matrix, row1, col1, row2, col2): 
    sum = 0 
    for row in range(row1, row2+1): 
        for col in range(col1, col2+1): 
            sum += matrix[row][col] 

    return sum 


print(sumRegion(matrix, 1, 1, 2, 2))



"""Optimal Solution"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix) , len(matrix[0]) 
        self.sumMat = [[0] *(cols+1) for row in range(rows+1)] 


        for r in range(rows): 
            prefix = 0
            for c in range(cols): 
                prefix += matrix[r][c] 
                above = self.sumMat[r][c+1] 
                self.sumMat[r+1][c+1] = prefix + above


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1 

        bottomRight = self.sumMat[r2][c2] 
        above = self.sumMat[r1-1][c2] 
        left = self.sumMat[r2][c1-1]

        leftTop = self.sumMat[r1-1][c1-1] 

        return bottomRight - above - left + leftTop
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)