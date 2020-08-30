# Runtime: 436 ms, faster than 49.63% of Python online submissions for Implement Rand10() Using Rand7().
# Memory Usage: 17.8 MB, less than 58.39% of Python online submissions for Implement Rand10() Using Rand7().

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        
        ids = 41
        
        while ids > 40:
            row = rand7()
            col = rand7()
            
            ids = col + (row-1) * 7
        
        return 1 + ids%10