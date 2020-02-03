class Solution:
    """
    @param M: the 01 matrix
    @return: the longest line of consecutive one in the matrix
    """
    def longestLine(self, M):
        # Write your code here
        
        m = len(M)
        if m == 0:
            return 0
        
        n = len(M[0])
        
        dp = [[[0 for x in range(4)] for y in range(n)] for z in range(m)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                
                if j-1 >= 0:
                    dp[i][j][0] = dp[i][j-1][0] + 1
                else:
                    dp[i][j][0] = 1
              
                ans = max(ans, dp[i][j][0])
                
                if i-1 >= 0:
                    dp[i][j][2] = dp[i-1][j][2] + 1
                else:
                    dp[i][j][2] = 1
                
                ans = max(ans, dp[i][j][2])
                
                if i-1 >=0 and j-1 >= 0:
                    dp[i][j][1] = dp[i-1][j-1][1] + 1
                else:
                    dp[i][j][1] = 1
                
                ans = max(ans, dp[i][j][1])
                
                if i+1 < m and j+1 < n:
                    dp[i][j][3] = dp[i+1][j+1][3] + 1
                else:
                    dp[i][j][3] = 1
                
                ans = max(ans, dp[i][j][3])
        
        return ans