# Runtime: 12 ms, faster than 89.46% of Python online submissions for Rectangle Overlap.
# Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Rectangle Overlap.

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3]:
            return False
        return True