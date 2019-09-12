# Runtime: 16 ms, faster than 95.47% of Python online submissions for Arranging Coins.
# Memory Usage: 11.8 MB, less than 14.29% of Python online submissions for Arranging Coins.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 1
        r = pow(2,32)
        
        while l <= r:
                           
            m = (l++r)/2
            
            x = m*(m+1)/2
            
            # print l,m,r,x,n
            
            if n < x:
                r = m - 1
            elif n > x:
                l = m + 1
            else:
                return m
        
        return r