# Runtime: 56 ms, faster than 84.50% of Python online submissions for Transpose Matrix.
# Memory Usage: 12.3 MB, less than 66.67% of Python online submissions for Transpose Matrix.

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(A)
        if m == 0:
            return []
        n = len(A[0])
        
        new = []
        for i in range(n):
            new.append([A[x][i] for x in range(m)])
        
        return new