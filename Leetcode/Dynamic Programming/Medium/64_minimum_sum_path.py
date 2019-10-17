# Runtime: 84 ms, faster than 52.14% of Python online submissions for Minimum Path Sum.
# Memory Usage: 13.1 MB, less than 20.59% of Python online submissions for Minimum Path Sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[sys.maxint for i in range(n+1)] for _ in range(m+1)]
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                
                if i==m-1 and j==n-1:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min(grid[i][j]+dp[i+1][j], grid[i][j]+dp[i][j+1])
        
        return dp[0][0]