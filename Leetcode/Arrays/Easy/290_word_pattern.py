# Runtime: 12 ms, faster than 88.65% of Python online submissions for Word Pattern.
# Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Word Pattern.

class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        curr_el = 1
        d = {}
        s_patt = ""
        
        for i in pattern:
            if d.get(i) == None:
                d[i] = curr_el
                curr_el += 1
            
            s_patt += str(d[i])
        
        string = string.split()
        curr_el = 1
        d = {}
        s_str = ""
        
        for i in string:
            if d.get(i) == None:
                d[i] = curr_el
                curr_el += 1
            
            s_str += str(d[i])
            
        return s_patt == s_str
        
        