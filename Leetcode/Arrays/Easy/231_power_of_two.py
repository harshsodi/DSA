# Runtime: 16 ms, faster than 82.12% of Python online submissions for Power of Two.
# Memory Usage: 11.7 MB, less than 76.47% of Python online submissions for Power of Two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n < 2:
            return n == 1
        
        while n:
            if n!=1 and n%2 != 0:
                return False
        
            n = n/2
        
        return True