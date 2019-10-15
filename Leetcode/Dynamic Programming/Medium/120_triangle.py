# Runtime: 44 ms, faster than 71.28% of Python online submissions for Triangle.
# Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Triangle.

class Solution(object):
    
    def minimumTotal(self, a):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
                
        i = len(a)-2
        while i >= 0:
            for j in range(0, i+1):
                a[i][j] = min(a[i][j] + a[i+1][j], a[i][j] + a[i+1][j+1])
        
            i -= 1
        
        return a[0][0]