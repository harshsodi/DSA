# Runtime: 16 ms, faster than 99.00% of Python online submissions for Reverse Integer.
# Memory Usage: 11.6 MB, less than 87.76% of Python online submissions for Reverse Integer.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        mult = 1
        if x < 0:
            x = x*-1
            mult = -1
        
        pow10 = 0
        ans = 0
        
        while x > 0:
            ans = ans*10 + x%10
            pow10 += 1
            x /= 10
        
        if ans > pow(2,31) - 1 or ans < pow(2,31)*-1:
            return 0
        
        return ans * mult