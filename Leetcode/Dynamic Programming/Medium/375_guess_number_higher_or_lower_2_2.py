# Runtime: 972 ms, faster than 34.24% of Python online submissions for Guess Number Higher or Lower II.
# Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Guess Number Higher or Lower II.

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def get_dp(dp, s, e):
            if s < e:
                return dp[s][e]
            return 0
    
        dp = [[0 for j in range(n+1)] for j in range(n+1)]

        for diff in range(n+1):
            for i in range(1, (n-diff)+1):
                ans = float('inf')
                for x in range(i, i+diff):
                    ans = min(ans, x+max(get_dp(dp, i, x-1), get_dp(dp, x+1, i+diff)))
                dp[i][i+diff] = ans
        
        
        if dp[1][n] == float('inf'):
            return 0
        return dp[1][n]