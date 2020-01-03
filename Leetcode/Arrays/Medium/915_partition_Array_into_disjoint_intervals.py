# Runtime: 180 ms, faster than 60.81% of Python online submissions for Partition Array into Disjoint Intervals.
# Memory Usage: 15.2 MB, less than 66.67% of Python online submissions for Partition Array into Disjoint Intervals.

class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        
        minright = [0 for _ in range(n)]
        minright[n-1] = float('inf')
        
        curr_min = A[n-1]
        i = n-2
        while i >= 0:
            minright[i] = curr_min
            curr_min = min(curr_min, A[i])
            i -= 1
        
        curr_max = A[0]
        for i in range(n):
            curr_max = max(curr_max, A[i])
            
            if curr_max <= minright[i]:
                return i+1