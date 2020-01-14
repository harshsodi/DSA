# Runtime: 16 ms, faster than 68.82% of Python online submissions for Climbing Stairs.
# Memory Usage: 11.7 MB, less than 48.44% of Python online submissions for Climbing Stairs.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        f0 = 1
        f1 = 1
        
        ans = f0 + f1
        
        for i in range(2, n+1):
            ans = f0 + f1
            f0 = f1
            f1 = ans
        
        return ans