# Runtime: 156 ms, faster than 93.37% of Python online submissions for Car Fleet.
# Memory Usage: 14.1 MB, less than 40.00% of Python online submissions for Car Fleet.

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        n = len(position)
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        t = sorted(zip(position, speed))
        print t
        units = [(target-x[0])/(x[1]*1.0) for x in t]
        print units
        
        ans = 1
        
        i = n-2
        curr = units[n-1]
        
        while i >= 0:
            if units[i] > curr:
                curr = units[i]
                ans += 1
        
            i -= 1
        
        return ans