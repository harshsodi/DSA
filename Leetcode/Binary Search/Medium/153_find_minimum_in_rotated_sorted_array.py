# Runtime: 20 ms, faster than 96.25% of Python online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 11.9 MB, less than 71.43% of Python online submissions for Find Minimum in Rotated Sorted Array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n <=2:
            return min(nums)
        
        l = 0
        r = n-1
        
        pivot = 0
        
        while l < r:
            
            m = (l+r)/2
            
            if m == l or m == r:
                return min([nums[l], nums[r], nums[m]])
            
            if nums[m]  < nums[r]:
                r = m
            elif nums[m] > nums[l]:
                l = m