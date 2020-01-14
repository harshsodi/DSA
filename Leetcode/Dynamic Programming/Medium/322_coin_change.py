# Runtime: 1620 ms, faster than 12.99% of Python online submissions for Coin Change.
# Memory Usage: 12.7 MB, less than 15.00% of Python online submissions for Coin Change.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        coins = list(sorted(coins, reverse=True))
        
        if amount == 0:
            return 0
    
        if amount < coins[-1]:
            return -1
        
        inf = amount + 1
        lc = len(coins)
            
        dp = [[inf for _ in range(amount+1)] for x in range(lc)]
        
        for i in range(lc):
            dp[i][0] = 0
        
        for i in range(lc):
            for j in range(1, amount+1):
                amt = j
                c = coins[i]
                if j >= c:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-c] + 1)
        
        ans = dp[-1][-1]
        
        if ans == inf:
            return -1
        return ans