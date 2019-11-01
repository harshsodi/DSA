# Runtime: 44 ms, faster than 88.19% of Python online submissions for Search a 2D Matrix II.
# Memory Usage: 15.5 MB, less than 80.00% of Python online submissions for Search a 2D Matrix II.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        
        print m,n
        i = m - 1
        j = 0
        
        while i>=0 and j<n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        
        return False