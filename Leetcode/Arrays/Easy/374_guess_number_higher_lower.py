# Runtime: 16 ms, faster than 66.14% of Python online submissions for Guess Number Higher or Lower.
# Memory Usage: 11.7 MB, less than 51.85% of Python online submissions for Guess Number Higher or Lower.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 1
        r = n
        
        while l <= r:
            m = (l+r)/2
            g = guess(m)
            
            # print l, m, r
            
            if g == 0:
                return m
            elif g == -1:
                r = m-1
            else:
                l = m+1