# Runtime: 64 ms, faster than 88.45% of Python online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 13.8 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        sh = 0
        
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                sh += 1
            else:
                nums[i-sh] = nums[i]
        
        return n-sh