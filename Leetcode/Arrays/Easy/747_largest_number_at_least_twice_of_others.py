# Runtime: 20 ms, faster than 83.57% of Python online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 11.7 MB, less than 44.44% of Python online submissions for Largest Number At Least Twice of Others.

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        max1 = -sys.maxint + 1
        max2 = -sys.maxint + 1
        
        h1 = 0
        
        for i in range(len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                h1 = i
            elif nums[i] > max2 and nums[i] != max1:
                max2 = nums[i]
        
        if max1 >= 2*max2:
            return h1
        else:
            return -1