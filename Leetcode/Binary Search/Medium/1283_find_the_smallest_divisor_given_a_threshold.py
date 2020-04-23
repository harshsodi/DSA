# Runtime: 380 ms, faster than 62.50% of Python online submissions for Find the Smallest Divisor Given a Threshold.
# Memory Usage: 19.2 MB, less than 100.00% of Python online submissions for Find the Smallest Divisor Given a Threshold.

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        from math import ceil
        
        l = 1
        r = max(nums)
        
        while l < r:
            m = (l+r) / 2
            
            a = [ceil(i*1.0/m) for i in nums]
            sm = sum(a)
            # print m, sm, a
            
            if sm > threshold:
                l = m + 1
            else:
                r = m
        
        return l