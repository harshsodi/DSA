# Runtime: 72 ms, faster than 94.42% of Python online submissions for Contains Duplicate II.
# Memory Usage: 16.6 MB, less than 31.50% of Python online submissions for Contains Duplicate II.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = {}
        
        for i in range(len(nums)):
            if d.get(nums[i]) != None and i-d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        
        return False