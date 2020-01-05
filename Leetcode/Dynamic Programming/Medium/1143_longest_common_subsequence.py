# Runtime: 364 ms, faster than 45.99% of Python online submissions for Longest Common Subsequence.
# Memory Usage: 20.5 MB, less than 100.00% of Python online submissions for Longest Common Subsequence.

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        n1 = len(text1)
        n2 = len(text2)
        
        dp = [[0 for _ in range(n2)] for x in range(n1)]
        
        for i in range(n1):
            for j in range(n2):
                if i == 0 or j == 0:
                    if text1[i] == text2[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i][max(0, j-1)], dp[max(0, i-1)][j])
                else:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    
        return dp[n1-1][n2-1]