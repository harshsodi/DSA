# Runtime: 140 ms, faster than 97.47% of Python online submissions for Assign Cookies.
# Memory Usage: 13.1 MB, less than 16.67% of Python online submissions for Assign Cookies.

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        
        gi = 0
        si = 0
        
        while gi < len(g) and si < len(s):
            
            if g[gi] <= s[si]:
                gi += 1
                si += 1
            
            else:
                si += 1
                
        return gi