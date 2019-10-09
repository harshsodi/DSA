# Runtime: 16 ms, faster than 66.01% of Python online submissions for Nth Digit.
# Memory Usage: 11.7 MB, less than 81.82% of Python online submissions for Nth Digit.

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<10:
            return n
        
        l = 0
        r = 9
        
        i=1
        while True:
            if n < r:
                break
            l = r+1
            r += 9*pow(10,i)*(i+1)
            
            i += 1
    
        diff = n - l
        seed = pow(10,i-1)
        seed += diff/(i)    
        char_num = diff%i
        
        return int(str(seed)[char_num])