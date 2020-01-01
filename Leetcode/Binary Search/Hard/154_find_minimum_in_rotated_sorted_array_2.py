# Runtime: 32 ms, faster than 96.24% of Python online submissions for Find Minimum in Rotated Sorted Array II.
# Memory Usage: 12.1 MB, less than 28.57% of Python online submissions for Find Minimum in Rotated Sorted Array II.

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
            
            while l < r and nums[l] == nums[r]:
                l += 1
            
            m = (l+r)/2
            print l, m, r
            
            if m == l or m == r:
                return min([nums[l], nums[r], nums[m]])
            
            if nums[m]  <= nums[r]:
                r = m
            elif nums[m] >= nums[l]:
                l = m