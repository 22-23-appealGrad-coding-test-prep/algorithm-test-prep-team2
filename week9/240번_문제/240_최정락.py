class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = 0 
        cols = len(matrix[0]) -1

        while(1):
            if target == matrix[rows][cols]:
                return True
            elif target > matrix[rows][cols]:
                rows += 1
            elif target < matrix[rows][cols]:
                cols -= 1
            if cols < 0 or rows == len(matrix):
                break
        
        return False