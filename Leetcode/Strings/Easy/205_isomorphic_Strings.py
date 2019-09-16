# Runtime: 28 ms, faster than 75.32% of Python online submissions for Isomorphic Strings.
# Memory Usage: 13.1 MB, less than 50.00% of Python online submissions for Isomorphic Strings.

class Solution(object):
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        d1 = {}
        d2 = {}
        
        act = 0
        bct = 0
        
        l = len(s)
        
        for i in range(l):
            
            c1 = s[i]
            c2 = t[i]
            
            d1g = d1.get(c1)
            d2g = d2.get(c2)
            
            if d1g != d2g:
                return False
            else:
                if d1g == None:
                    act += 1
                    d1[c1] = act
                if d2g == None:
                    bct += 1
                    d2[c2] = bct
        
        return True