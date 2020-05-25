# Runtime: 12 ms, faster than 98.68% of Python online submissions for Play with Chips.
# Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Play with Chips.

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        
        n = len(chips)
        
        e = 0
        o = 0
        
        for i in range(n):
            if chips[i] % 2:
                o += 1
            else:
                e += 1
                
        return min(o, e)