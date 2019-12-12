# Runtime: 4 ms, faster than 99.87% of Python online submissions for Bulb Switcher.
# Memory Usage: 11.8 MB, less than 25.00% of Python online submissions for Bulb Switcher.

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return int(math.floor(math.sqrt(n)))