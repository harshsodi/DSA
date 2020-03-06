# Runtime: 24 ms, faster than 70.68% of Python online submissions for H-Index.
# Memory Usage: 12 MB, less than 40.00% of Python online submissions for H-Index.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        
        citations= [0] +  list(sorted(citations, reverse=True))
        n += 1
        
        ans = 0
        for i in range(1,n):
            if citations[i] >= i:
                if i < n-1:
                    if citations[i+1] <= i:
                        ans = i
                else:
                    ans = i
        return ans