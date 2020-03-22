# Runtime: 632 ms, faster than 38.56% of Python online submissions for Count Square Submatrices with All Ones.
# Memory Usage: 13.8 MB, less than 100.00% of Python online submissions for Count Square Submatrices with All Ones.

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        dp = [[0 for _ in range(n)] for __ in range(m)]
        
        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j]
        
        ans = 0
        
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
        
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
        
        return ans