# Runtime: 16 ms, faster than 78.76% of Python online submissions for Unique Paths.
# Memory Usage: 11.7 MB, less than 65.52% of Python online submissions for Unique Paths.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        
        for i_ in range(m):
            for j_ in range(n):
                i = m - 1 - i_
                j = n - 1 - j_
                
                if i==m-1 and j==n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]