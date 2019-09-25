# Runtime: 28 ms, faster than 89.02% of Python online submissions for Distance Between Bus Stops.
# Memory Usage: 12.3 MB, less than 100.00% of Python online submissions for Distance Between Bus Stops.

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        
        n = len(distance)
        
        i = start
        s2d = 0
        while i != destination:
            s2d += distance[i]
            i = (i+1) % n
            
        d2s = 0
        while i != start:
            d2s += distance[i]
            i = (i+1) % n
        
        return min(s2d, d2s)
        