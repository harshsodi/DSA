# Runtime: 108 ms, faster than 64.60% of Python online submissions for Coin Change 2.
# Memory Usage: 12 MB, less than 33.33% of Python online submissions for Coin Change 2.

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        n = len(coins)
        
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        
        for i in range(n):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        
        return dp[-1]