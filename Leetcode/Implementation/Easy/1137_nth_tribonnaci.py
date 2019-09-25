# Runtime: 4 ms, faster than 99.45% of Python online submissions for N-th Tribonacci Number.
# Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for N-th Tribonacci Number.

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a = 0
        b = 1
        c = 1
        
        for i in range(n-2):
            d = a+b+c
            a = b
            b = c
            c = d
        
        return c