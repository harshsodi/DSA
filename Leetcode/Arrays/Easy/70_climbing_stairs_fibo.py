# Runtime: 16 ms, faster than 88/58% of Python online submissions for Climbing Stairs.
# Memory Usage: 11.5 MB, less than 100.00% of Python online submissions for Climbing Stairs.

class Solution(object):
    
    def climbStairs(self, target):
        """
        :type n: int
        :rtype: int
        """
        
        if target == 1:
            return 1
        
        m1 = 1
        m2 = 1
        
        c = 0
        s = 0
        
        while c < target-1:
            s = m1 + m2
            m2 = m1
            m1 = s
            c += 1
        
        return s