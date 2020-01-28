# Runtime: 140 ms, faster than 37.75% of Python online submissions for Repeated String Match.
# Memory Usage: 11.9 MB, less than 66.67% of Python online submissions for Repeated String Match.

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        n = len(A)
        m = len(B)
        
        if m < n:
            if B in A:
                return 1
            elif B in A*2:
                return 2
            else:
                return -1
        
        i = 1
        a = A
        while len(A) < m:
            A += a
            i += 1
        
        if B in A:
            return i
        elif B in A+a:
            return i+1
    
        return -1