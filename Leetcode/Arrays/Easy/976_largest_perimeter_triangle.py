# Runtime: 180 ms, faster than 80.72% of Python online submissions for Largest Perimeter Triangle.
# Memory Usage: 12.8 MB, less than 36.36% of Python online submissions for Largest Perimeter Triangle.

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        A = sorted(A, reverse=True)
        
        for i in range(n-2):
            if A[i+1] + A[i+2] > A[i]:
                return A[i+1] + A[i+2] + A[i]
        
        return 0