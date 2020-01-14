# Runtime: 52 ms, faster than 100.00% of Python online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Decompress Run-Length Encoded List.

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        
        ans = []
        
        i = 1
        while i < n:
            ans += [nums[i]] * nums[i-1]
            i += 2
        
        return ans