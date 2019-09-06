# Runtime: 160 ms, faster than 61.87% of Python online submissions for Majority Element.
# Memory Usage: 13.3 MB, less than 75.61% of Python online submissions for Majority Element.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        half_l = l/2
        
        d = {}
        
        for i in nums:
            d[i] = d.get(i,0) + 1
            if d[i] > half_l:
                return i