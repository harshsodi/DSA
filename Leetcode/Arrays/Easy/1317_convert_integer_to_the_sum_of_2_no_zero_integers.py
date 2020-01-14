# Runtime: 8 ms, faster than 99.25% of Python online submissions for Convert Integer to the Sum of Two No-Zero Integers.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Convert Integer to the Sum of Two No-Zero Integers.

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        def check(num):
            while num:
                if num%10 == 0:
                    return False
                num /= 10
            return True
        
        i = 1
        
        while i < n:
            if check(i) and check(n-i):
                return [n-i, i]
        
            i *= 2