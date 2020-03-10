Details 
# Runtime: 2096 ms, faster than 23.60% of Python online submissions for Longest Arithmetic Sequence.
# Memory Usage: 317.6 MB, less than 83.33% of Python online submissions for Longest Arithmetic Sequence.

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        d = {}
        
        ans = 0
        
        for i in range(1, n):
            for j in range(0, i):
                diff = A[i] - A[j] 
                d[(i, diff)] = d.get((j, diff), 1) + 1
        
                ans = max(ans, d[(i, diff)])
        
        return ans