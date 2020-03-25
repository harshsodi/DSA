# Runtime: 540 ms, faster than 63.02% of Python online submissions for Image Overlap.
# Memory Usage: 11.9 MB, less than 50.00% of Python online submissions for Image Overlap.

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        
        n = len(A)
        gans = 0
        
        for i in range(n):
            for j in range(n):
                ans = 0
                for x in range(i+1):
                    for y in range(j+1):
                        # print i, j, x, y, n-1-i+x, n-j-1+y 
                        if B[n-1-i+x][n-1-j+y] == 1 and A[x][y] == 1:
                            ans += 1
                # print ans
                gans = max(ans, gans)
        
        for i in range(n):
            for j in range(n):
                ans = 0
                for x in range(i+1):
                    for y in range(j+1):
                        # print i, j, x, y, n-1-i+x, n-j-1+y 
                        if A[n-1-i+x][n-1-j+y] == 1 and B[x][y] == 1:
                            ans += 1
                # print ans
                gans = max(ans, gans)
        
        return gans