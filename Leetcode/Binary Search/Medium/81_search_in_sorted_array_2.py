# Runtime: 40 ms, faster than 66.62% of Python online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 12.1 MB, less than 17.65% of Python online submissions for Search in Rotated Sorted Array II.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
            
        n = len(nums)
        
        if n == 0:
            return False
        
        l = 0
        r = n-1
        
        if nums[l] == target:
            return True
        if nums[r] == target:
            return True
        
        while l < r:
            
            m = (l+r)/2
            # print l, m, r
            
            if nums[l] == target:
                return True
            if nums[r] == target:
                return True
        
            if nums[m] == target:
                return True
            
            if nums[l] < nums[r]:
                # All good (sub)array
                if nums[m] < target:
                    l = m+1
                else:
                    r = m
            else:
                while l < r and nums[l] == nums[r]:
                    l += 1
                    r -= 1
                
                if nums[l] == target:
                    return True
                if nums[r] == target:
                    return True    
            
                if nums[m] >= nums[l]:
                    if target > nums[l] and target < nums[m]:
                        r = m
                    else:
                        l = m+1
                else:
                    if target > nums[m] and target < nums[r]:
                        l = m+1
                    else:
                        r = m
        
        return False