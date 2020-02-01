# Runtime: 108 ms, faster than 28.65% of Python online submissions for Smallest Range I.
# Memory Usage: 12.7 MB, less than 42.86% of Python online submissions for Smallest Range I.

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        mx = float('-inf')
        mn = float('inf')
        
        for i in A:
            mx = max(i, mx)
            mn = min(i, mn)
        
        return max(0, (mx - mn) - 2*K)