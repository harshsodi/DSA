# Runtime: 12 ms, faster than 94.36% of Python online submissions for Integer Replacement.
# Memory Usage: 11.7 MB, less than 72.73% of Python online submissions for Integer Replacement.

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        op = 0
        
        while n > 1:
            op += 1
            if n%2 == 0:
                n /= 2
            else:
                if n%4 == 3 and n != 3:
                    n += 1
                else:
                    n -= 1
            
        return op