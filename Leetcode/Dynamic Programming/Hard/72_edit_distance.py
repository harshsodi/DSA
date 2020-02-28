# Runtime: 168 ms, faster than 29.98% of Python online submissions for Edit Distance.
# Memory Usage: 15 MB, less than 25.00% of Python online submissions for Edit Distance.

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        
        if n == 0:
            return m
        
        dp = [[0 for x in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1
        
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1] + 1
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
            
        return dp[m][n]