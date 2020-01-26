# Runtime: 72 ms, faster than 17.43% of Python online submissions for Swap Adjacent in LR String.
# Memory Usage: 12.3 MB, less than 28.57% of Python online submissions for Swap Adjacent in LR String.

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        
        n = len(start)
        
        start_c  = []
        start_i = []
        
        end_c = []
        end_i = []
        
        for i in range(n):
            if start[i] != 'X':
                start_c.append(start[i])
                start_i.append(i)
            
            if end[i] != 'X':
                end_c.append(end[i])
                end_i.append(i)
        
        if start_c == end_c:
            for i in range(len(start_c)):
                if end_c[i] == 'L' and end_i[i] > start_i[i]:
                    return False
                if end_c[i] == 'R' and end_i[i] < start_i[i]:
                    return False
                
            return True
    
        return False