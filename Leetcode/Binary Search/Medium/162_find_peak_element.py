# Runtime: 28 ms, faster than 92.12% of Python online submissions for Find Peak Element.
# Memory Usage: 12.9 MB, less than 8.11% of Python online submissions for Find Peak Element.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = [float('-inf')] + nums + [float('-inf')]
        n = len(nums)
        
        l = 1
        r = n - 2
        
        while l < r:
            
            if nums[l-1] < nums[l] > nums[l+1]:
                return l-1
            
            if nums[r-1] < nums[r] > nums[r+1]:
                return r-1
        
            m = (l+r)/2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m-1
            
            if nums[m-1] > nums[m]:
                r = m-1
            else:
                l = m + 1
        
        return l-1