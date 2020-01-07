# Runtime: 388 ms, faster than 66.67% of Python online submissions for Shortest Common Supersequence .
# Memory Usage: 20.6 MB, less than 100.00% of Python online submissions for Shortest Common Supersequence .

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        n1 = len(str1)
        n2 = len(str2)
        
        dp = [[0 for _ in range(n2+1)] for x in range(n1+1)]
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
        i = n1
        j = n2
        ans = ""
       
        while i > 0 or j > 0:
            if i == 0:
                ans = str2[j-1] + ans
                j -= 1
            elif j == 0:
                ans = str1[i-1] + ans
                i -= 1
            elif str1[i-1] == str2[j-1]:
                ans = str1[i-1] + ans
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                ans = str1[i-1] + ans
                i -= 1
            elif dp[i][j] == dp[i][j-1]:
                ans = str2[j-1] + ans
                j -= 1
        
        return ans            