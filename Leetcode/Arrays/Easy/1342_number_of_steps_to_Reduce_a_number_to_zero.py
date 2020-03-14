# Runtime: 16 ms, faster than 73.81% of Python online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Number of Steps to Reduce a Number to Zero.

class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        ans = 0
        while num:
            ans += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        
        return ans