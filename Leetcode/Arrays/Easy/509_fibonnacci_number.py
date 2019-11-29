# Runtime: 20 ms, faster than 55.79% of Python online submissions for Fibonacci Number.
# Memory Usage: 11.6 MB, less than 84.78% of Python online submissions for Fibonacci Number.

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        a = 1
        b = 1
        
        for i in range(2, N):
            c = a+b
            a = b
            b = c
        
        return b