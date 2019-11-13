# Runtime: 352 ms, faster than 42.07% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 18.6 MB, less than 73.33% of Python online submissions for Find All Duplicates in an Array.

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        ans = []
        for i in range(0,n):
            x = abs(nums[i])-1
            
            if nums[x] < 0:
                ans.append(abs(nums[i]))
            
            nums[x] *= -1
        
        return ans