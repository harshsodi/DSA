# Runtime: 60 ms, faster than 37.21% of Python online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 12.9 MB, less than 50.00% of Python online submissions for Bitwise AND of Numbers Range.

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
                    
        def get_inc(n):
            i = 0
            while n > 0 and n % 2 == 0:
                i += 1
                n /= 2
            
            return pow(2, i)
    
        ans = m
        i = m
        
        while i <= n:
            ans &= i
            
            i += get_inc(i)
        
        return ans