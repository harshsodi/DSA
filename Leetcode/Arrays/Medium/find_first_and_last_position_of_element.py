# Runtime: 64 ms, faster than 90.60% of Python online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 12.9 MB, less than 96.37% of Python online submissions for Find First and Last Position of Element in Sorted Array.

class Solution(object):
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        size = len(nums)
        if size == 0:
            return [-1, -1]
        
        lo = 0
        hi = size -1
        
        a1 = -1
        a2 = -1
        
        while lo <= hi:
            mid = (lo + hi) / 2
            
            if nums[mid] == target:
                a1 = mid
            
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if a1 == -1:
            return [-1, -1]
        
        lo = 0
        hi = size - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            
            if nums[mid] == target:
                a2 = mid
            
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return [a1, a2]