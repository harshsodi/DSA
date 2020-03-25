# Runtime: 32 ms, faster than 92.69% of Python online submissions for Flipping an Image.
# Memory Usage: 11.8 MB, less than 30.00% of Python online submissions for Flipping an Image.

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(A)
        if m == 0:
            return []
        n = len(A[0])
        
        for i in range(m):
            for j in range((n+1)/2):
                A[i][j], A[i][n-1-j] = 1-A[i][n-1-j], 1-A[i][j]
        
        return A