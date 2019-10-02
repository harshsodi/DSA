# Runtime: 100 ms, faster than 86.28% of Python online submissions for Product of Array Except Self.
# Memory Usage: 17 MB, less than 95.24% of Python online submissions for Product of Array Except Self.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        
        if n < 3:
            nums.reverse()
            return [_ for _ in nums]
        
        a = [1 for _ in nums]
        b = [1 for _ in nums]
        
        lp = nums[0]
        rp = nums[n-1]
        
        i = 1
        while i<n:
            a[i] = lp
            lp *= nums[i]
            i += 1
        
        i = n-2
        while i >= 0:
            a[i] *= rp
            rp *= nums[i]
            i -= 1
        
        return a