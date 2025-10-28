class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix)-1  
        while top <= bottom: 
            mid_row = (top+bottom) //2 
            if target > matrix[mid_row][-1]: 
                top = mid_row + 1 
            elif target < matrix[mid_row][0]: 
                bottom = mid_row - 1
            else:
                break  

        if top>bottom: 
            return False 

        l,r  = 0, len(matrix[0])-1 
        while l<=r: 
            mid_col = (l+r) //2 
            if target == matrix[mid_row][mid_col]:
                return True
            elif target > matrix[mid_row][mid_col]: 
                l = mid_col + 1 
            else: 
                r = mid_col - 1 

        return False 


