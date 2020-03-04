# Runtime: 20 ms, faster than 75.03% of Python online submissions for Happy Number.
# Memory Usage: 11.9 MB, less than 7.50% of Python online submissions for Happy Number.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def f(k):
            ans = 0
            while k != 0:
                m = k%10
                ans += m*m
                k /= 10
            
            return ans
            
        mem = {}
        while True:
            
            if mem.get(n) != None:
                return False
            
            if n == 1:
                return True
            
            mem[n] = True
            
            n = f(n)