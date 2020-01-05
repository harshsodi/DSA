# Runtime: 2448 ms, faster than 12.48% of Python online submissions for Longest Palindromic Subsequence.
# Memory Usage: 27.1 MB, less than 33.33% of Python online submissions for Longest Palindromic Subsequence.

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        
        dp = [[0 for x in s] for _ in s]
        ans = 0
        
        for i in range(n):
            dp[i][i] = 1
            ans = 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
            else:
                dp[i][i+1] = 1
        
            ans = max(ans, dp[i][i+1])
        
        for offset in range(2, n+1):
            for i in range(0, n-offset):
                l = i
                r = i+offset
                
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l][r-1], dp[l+1][r])
        
                ans = max(ans, dp[l][r])
        
        return ans            