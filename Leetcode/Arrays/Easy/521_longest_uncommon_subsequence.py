# Runtime: 20 ms, faster than 36.42% of Python online submissions for Longest Uncommon Subsequence I .
# Memory Usage: 11.8 MB, less than 20.00% of Python online submissions for Longest Uncommon Subsequence I .

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        la = len(a)
        lb = len(b)
        
    
        if la != lb:
            return max(la,lb)
        
        if a == b:
            return -1
        else:
            return la