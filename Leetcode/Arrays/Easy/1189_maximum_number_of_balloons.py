# Runtime: 20 ms, faster than 86.87% of Python online submissions for Maximum Number of Balloons.
# Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Maximum Number of Balloons.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        d = {}
        
        for i in text:
            d[i] = d.get(i, 0) + 1
            
        return min(d.get("b", 0)/1, d.get("a", 0)/1, d.get("l", 0)/2, d.get("o", 0)/2, d.get("n", 0)/1)