# Runtime: 12 ms, faster than 97.37% of Python online submissions for Backspace String Compare.
# Memory Usage: 11.9 MB, less than 8.00% of Python online submissions for Backspace String Compare.

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        s = []
        for i in S:
            if i == "#":
                if len(s):
                    s.pop()
            else:
                s.append(i)
                

        t = []
        for i in T:
            if i == "#":
                if len(t):
                    t.pop()
            else:
                t.append(i)
               
        return s == t