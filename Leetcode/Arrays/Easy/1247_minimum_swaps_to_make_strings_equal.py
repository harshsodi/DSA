# Runtime: 12 ms, faster than 96.53% of Python online submissions for Minimum Swaps to Make Strings Equal.
# Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Minimum Swaps to Make Strings

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        m = len(s1)
        n = len(s2)
        
        if m != n: 
            return -1
                
        yx = 0
        xy = 0
        
        for i in range(m):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1
        
        if (xy + yx) %2 != 0:
            return -1
    
        return xy/2 + yx/2 + (xy%2)*2