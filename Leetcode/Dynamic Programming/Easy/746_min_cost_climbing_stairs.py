# Runtime: 36 ms, faster than 95.19% of Python online submissions for Min Cost Climbing Stairs.
# Memory Usage: 11.9 MB, less than 23.81% of Python online submissions for Min Cost Climbing Stairs.

class Solution(object):
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        dp = [0 for i in range(n+1)]
        
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]