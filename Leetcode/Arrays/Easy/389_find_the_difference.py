# Runtime: 16 ms, faster than 93.00% of Python online submissions for Find the Difference.
# Memory Usage: 11.7 MB, less than 54.55% of Python online submissions for Find the Difference.

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        sum_s = 0
        sum_t = 0
        
        l = len(s)
        i = -1
        
        for i in range(l):
            sum_s += ord(s[i])
            sum_t += ord(t[i])        
            
        sum_t += ord(t[i+1])
        
        return chr(sum_t - sum_s)