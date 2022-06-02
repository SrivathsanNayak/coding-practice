class Solution(object):
    def searchMatrix(self, matrix, target):
        
        
        #for one row or one column matrix
        if len(matrix[0]) == 1 or len(matrix) == 1:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
        
        #check last element of each row
        
        for row in matrix:
            if row[-1] >= target:
                return target in row
        
        return False
        