# Runtime: 732 ms, faster than 99.30% of Python online submissions for Distribute Candies.
# Memory Usage: 13.5 MB, less than 66.67% of Python online submissions for Distribute Candies.

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        num_can = len(candies)
        num_cat = len(set(candies))    
        num_each = (num_can + 1) / 2
        
        return min(num_cat, num_each)