# Runtime: 16 ms, faster than 90.30% of Python online submissions for Wiggle Subsequence.
# Memory Usage: 11.9 MB, less than 20.00% of Python online submissions for Wiggle Subsequence.

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Start with increasing
        
        n = len(nums)
        
        if n <= 1:
            return n
        
        inc = True
        if nums[1] < nums[0]:
            inc = False
        
        ans = 1
        inc = None
        
        for i in range(1, n):
            if nums[i] < nums[i-1] and inc != False: # Peak
                ans += 1
                inc = False
            elif nums[i] > nums[i-1] and inc != True:
                ans += 1
                inc = True
                
        return ans