# Runtime: 44 ms, faster than 83.95% of Python online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 12.7 MB, less than 32.56% of Python online submissions for Best Time to Buy and Sell Stock II.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        prices.append(0)
        
        p = 0
        pr = 0
        
        maxprof = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[pr]:
                # maxprof = max(maxprof, prices[pr] - prices[p])
                maxprof += prices[pr] - prices[p]
                p = i
            
            pr = i
    
        return maxprof