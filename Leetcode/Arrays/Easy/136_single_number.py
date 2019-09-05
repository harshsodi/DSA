# Runtime: 68 ms, faster than 75.08% of Python online submissions for Single Number.
# Memory Usage: 14.3 MB, less than 14.86% of Python online submissions for Single Number.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        s = 0
        
        for i in nums:
            if d.get(i):
                s -= i
            else:
                d[i] = True
                s += i
        
        return s