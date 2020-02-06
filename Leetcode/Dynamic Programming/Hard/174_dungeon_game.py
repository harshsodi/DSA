# Runtime: 56 ms, faster than 79.26% of Python online submissions for Dungeon Game.
# Memory Usage: 12.5 MB, less than 50.00% of Python online submissions for Dungeon Game.

class Solution(object):
    def calculateMinimumHP(self, d):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        m = len(d)
        n = len(d[0])
        
        dp = [[0 for x in range(n)] for y in range(m)]
        
        i = m-1
        
        while i >= 0:
            j = n-1
            while j >= 0:
                
                if d[i][j] <= 0:
                    dp[i][j] = -d[i][j] + 1
                
                if i < m-1 and j < n-1:
                    dp[i][j] = max(1, min([dp[i+1][j], dp[i][j+1]]) - d[i][j])
                elif i < m-1:
                    dp[i][j] = max(1, dp[i+1][j] - d[i][j])
                elif j < n-1:
                    dp[i][j] = max(1, dp[i][j+1] - d[i][j])
                elif d[i][j] > 0:
                    dp[i][j] = 1
                
                j -= 1
            
            i -= 1
        
        return dp[0][0]