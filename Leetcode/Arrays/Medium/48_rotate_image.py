# Runtime: 20 ms, faster than 79.27% of Python online submissions for Rotate Image.
# Memory Usage: 11.8 MB, less than 32.43% of Python online submissions for Rotate Image.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for i in range(((n+1)/2)):
            for j in range(i, n-i-1):
                on_row = i
                tw_col = n-i-1
                th_row = n-i-1
                fo_col = i
                
                last = matrix[n-1-j][fo_col]
                matrix[n-1-j][fo_col] = matrix[th_row][n-1-j]
                matrix[th_row][n-1-j] = matrix[j][tw_col]
                matrix[j][tw_col] = matrix[on_row][j]
                matrix[on_row][j] = last