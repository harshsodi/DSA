# Runtime: 120 ms, faster than 73.02% of Python online submissions for Is Subsequence.
# Memory Usage: 19 MB, less than 75.00% of Python online submissions for Is Subsequence.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == "":
            return True
        
        spointer = 0
        l = len(s)

        for i in t:
            
            if spointer >= l:
                return True
            
            if i == s[spointer]:
                spointer += 1
                
        return spointer == l