# Runtime: 140 ms, faster than 7.99% of Python online submissions for Minimum Size Subarray Sum.
# Memory Usage: 14.8 MB, less than 5.13% of Python online submissions for Minimum Size Subarray Sum.

class Solution(object):
    
    def __init__(self):
        pass
    
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        l = len(nums)
        sums = [None for _ in range(l)]
        
        min_len = l + 1
        
        sums[0] = nums[0]
        for i in range(1, l):
            sums[i] = sums[i-1] + nums[i]
        
        for i in range(l):
            
            left = i
            right = l-1
            
            x = None
            
            while left <= right:
                
                middle = (left+right)/2
                x = sums[middle] - sums[i] + nums[i]
                
                if x == s:
                    break
                elif x > s:
                    right = middle - 1
                else:
                    left = middle + 1
            
            if x >= s:
                min_len = min(min_len, middle - i + 1)
            
        if min_len > l:
            return "0"
        else:
            return min_len