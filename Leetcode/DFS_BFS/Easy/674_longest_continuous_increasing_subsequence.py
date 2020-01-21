# Runtime: 56 ms, faster than 92.04% of Python online submissions for Longest Continuous Increasing Subsequence.
# Memory Usage: 12.8 MB, less than 75.00% of Python online submissions for Longest Continuous Increasing Subsequence.

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n < 2:
            return n
        
        maxlen = 0
        
        i = 0
        j = 1
        
        while j < n:
            if nums[j] <= nums[j-1]:
                maxlen = max(maxlen, j - i)
                i = j
            
            j += 1
        
        maxlen = max(maxlen, j - i)
        
        return maxlen