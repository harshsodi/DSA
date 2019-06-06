def get_rc(i, m, n):
    c = i%n
    r = i%m
    
    return (r, c)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m*n - 1
        
        while left <= right:
            
            mid = (left + right) / 2
            element = matrix[mid/n][mid%n]
            
            if element > target:
                right = mid - 1
            elif element < target:
                left = mid + 1
            else:
                return True
        
        return False