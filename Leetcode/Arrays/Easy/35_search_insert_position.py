# Runtime: 32 ms, faster than 86.33% of Python online submissions for Search Insert Position.
# Memory Usage: 12.3 MB, less than 19.30% of Python online submissions for Search Insert Position.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = len(nums)
        for i in range(l):
            if nums[i] >= target:
                return i
            
        return l