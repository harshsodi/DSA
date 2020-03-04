# Runtime: 24 ms, faster than 56.66% of Python online submissions for First Missing Positive.
# Memory Usage: 11.7 MB, less than 55.88% of Python online submissions for First Missing Positive.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        for i in range(n):
            if nums[i]  <= 0:
                nums[i] = n+1
            
        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i]) - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1