# Runtime: 3964 ms, faster than 26.69% of Python online submissions for Longest Palindromic Substring.
# Memory Usage: 20.6 MB, less than 5.48% of Python online submissions for Longest Palindromic Substring.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        
        # dp = [[0,..,0], [0,..,0]]
        dp = [[0 for i in range(n)] for i in range(n)]
        
        maxl = 1
        maxrange = [0,0]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                maxrange = [i, i+1]
                maxl = 2
        
        l = 2
        while l < n:
            for i in range(n-l):
                x = i
                y = i+l
                
                if dp[x+1][y-1] == 1 and s[x] == s[y]:
                    dp[x][y] = 1
                    if maxl < y-x+1:
                        maxl = y-x+1
                        maxrange = [x, y]
        
            l += 1
        
        
        return s[maxrange[0]: maxrange[1]+1]