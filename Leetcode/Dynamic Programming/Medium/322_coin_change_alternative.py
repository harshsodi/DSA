# Runtime: 1196 ms, faster than 39.01% of Python online submissions for Coin Change.
# Memory Usage: 11.9 MB, less than 77.50% of Python online submissions for Coin Change.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        
        coins = sorted(coins)
        
        for i in range(1, amount+1):
            min_val = float('inf')
            f = False
            for c in coins:
                
                if c > i:
                    break
                
                if dp[i-c] != -1:
                    min_val = min(min_val, dp[i-c] + 1)
                    f = True
            
            if f:
                dp[i] = min_val
        
        return dp[-1]