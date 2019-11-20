# Runtime: 112 ms, faster than 86.11% of Python online submissions for Set Matrix Zeroes.
# Memory Usage: 12.4 MB, less than 21.74% of Python online submissions for Set Matrix Zeroes.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        if m == 0:
            return
        n  = len(matrix[0])
        
        r = None
        c = None
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if r != None:
                        matrix[r][j] = 0
                        matrix[i][c] = 0
                    else:
                        r = i
                        c = j
      
        if r == None:
            return
    
        
        for i in range(0,m):
            if i != r and matrix[i][c] == 0:
                for j in range(n):
                    matrix[i][j] = 0
                    
        for i in range(0,n):
            if i != c and matrix[r][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
    
        for i in range(m):
            matrix[i][c] = 0

        for i in range(n):
            matrix[r][i] = 0