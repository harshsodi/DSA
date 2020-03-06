# Runtime: 124 ms, faster than 83.33% of Python online submissions for H-Index II.
# Memory Usage: 16.7 MB, less than 37.50% of Python online submissions for H-Index II.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        
        if n == 1:
            if citations[0] == 0:
                return 0
            return 1
        
        l = 0
        r = n-1
        
        ans = 0
        
        while l <= r:
            m = (l+r)/2
            
            req = n-m
            
            if citations[m] < req:
                l = m+1
            else:
                ans = n-m
                r = m-1            
        
        return ans