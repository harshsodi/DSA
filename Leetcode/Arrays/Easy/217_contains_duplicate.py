# Runtime: 100 ms, faster than 95.05% of Python online submissions for Contains Duplicate.
# Memory Usage: 17.7 MB, less than 23.59% of Python online submissions for Contains Duplicate.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        d = {}
        
        for i in nums:
            if d.get(i):
                return True
            d[i] = True
        
        return False