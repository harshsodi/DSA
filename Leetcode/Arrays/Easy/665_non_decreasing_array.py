# Runtime: 276 ms, faster than 5.29% of Python online submissions for Non-decreasing Array.
# Memory Usage: 12.7 MB, less than 60.00% of Python online submissions for Non-decreasing Array.

class Solution(object):
    
    def f(self, nums, duped):
        
        print "Testing ", nums
        
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                if duped:
                    print "Bad"
                    return False
                else:
                    return self.f(nums[:i] + [nums[i+1]] + nums[i+1:], True) or self.f(nums[:i+1] + [nums[i]] + nums[i+2:], True)
                
        return True
    
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return self.f(nums, False)