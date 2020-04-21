# Runtime: 1012 ms, faster than 86.45% of Python online submissions for Subarray Product Less Than K.
# Memory Usage: 16.7 MB, less than 14.29% of Python online submissions for Subarray Product Less Than K.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k <= 1:
            return 0
        
        n = len(nums)
        
        l = 0
        ans = 0
        
        sm = 1
        
        for r in range(n):
            sm *= nums[r]
            while sm >= k:
                sm /= nums[l]
                l += 1
        
            ans += r-l+1
        
        return ans
            