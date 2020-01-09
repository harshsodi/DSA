# Runtime: 24 ms, faster than 87.66% of Python online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12 MB, less than 34.69% of Python online submissions for Search in Rotated Sorted Array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 0:
            return -1
        
        l = 0
        r = n-1
        
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        while l < r:
            
            m = (l+r)/2
            print l, m, r
            
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
        
            if nums[m] == target:
                return m
            
            if nums[l] < nums[r]:
                # All good (sub)array
                if nums[m] < target:
                    l = m+1
                else:
                    r = m
            else:
                if nums[m] > nums[l]: # /\
                    if target > nums[l] and target < nums[m]:
                        r = m
                    else:
                        l = m+1
                else: # \/
                    if target > nums[m] and target < nums[r]:
                        l = m+1
                    else:
                        r = m
                    
        return -1