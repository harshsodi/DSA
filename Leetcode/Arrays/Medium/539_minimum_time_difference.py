# Runtime: 76 ms, faster than 36.76% of Python online submissions for Minimum Time Difference.
# Memory Usage: 15 MB, less than 100.00% of Python online submissions for Minimum Time Difference.

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        a = []
        for t in timePoints:
            x = t.split(":")
            h = int(x[0])
            m = int(x[1])
            
            final = h*60 + m
            a.append(final)

        a = sorted(a)
        a.append(a[0])
        
        ans = float('inf')
        
        for i in range(1, len(a)):
            diff = min(abs(a[i] - a[i-1]), 1440 - abs(a[i] - a[i-1]))
            ans = min(ans, diff)
    
        return ans