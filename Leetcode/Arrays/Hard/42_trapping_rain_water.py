# Runtime: 36 ms, faster than 75.43% of Python online submissions for Trapping Rain Water.
# Memory Usage: 12.2 MB, less than 75.34% of Python online submissions for Trapping Rain Water.

class Solution(object):
    def trap(self, a):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(a)
        
        if n == 0:
            return 0
        
        lwa = [_ for _ in a]
        rwa = [_ for _ in a]
        
        lw = a[0]
        rw = a[n-1]
        
        for i in range(n):
            if a[i] > lw:
                lw = a[i]
            else:
                lwa[i] = lw
                
        for i in range(n):
            if a[n-1-i] > rw:
                rw = a[n-1-i]
            else:
                rwa[n-1-i] = rw
                
        vol = 0
        for i in range(n):
            vol += min(abs(a[i] - lwa[i]), abs(a[i] - rwa[i]))
        
        return vol