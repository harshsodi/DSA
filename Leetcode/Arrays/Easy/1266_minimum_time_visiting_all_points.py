# Runtime: 40 ms, faster than 86.01% of Python online submissions for Minimum Time Visiting All Points.
# Memory Usage: 12 MB, less than 100.00% of Python online submissions for Minimum Time Visiting All Points.

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)
        
        ans = 0
        
        for i in range(1, n):
            
            xdiff = abs(points[i][0] - points[i-1][0])
            ydiff = abs(points[i][1] - points[i-1][1])
            
            mx = max(ydiff, xdiff)
            mn = min(ydiff, xdiff)
            
            ans += abs(mn) + abs(mx - mn)
            
        return ans