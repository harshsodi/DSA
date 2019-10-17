# Runtime: 24 ms, faster than 97.24% of Python online submissions for Unique Paths II.
# Memory Usage: 12 MB, less than 10.53% of Python online submissions for Unique Paths II.

class Solution(object):
    
    def uniquePathsWithObstacles(self, a):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(a)
        n = len(a[0])
        
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        
        for i_ in range(m):
            for j_ in range(n):
                i = m - 1 - i_
                j = n - 1 - j_
                
                if i==m-1 and j==n-1 and a[i][j] == 0:
                    dp[i][j] = 1
                elif a[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]