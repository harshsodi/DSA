# Runtime: 24 ms, faster than 38.20% of Python online submissions for Sort Colors.
# Memory Usage: 11.7 MB, less than 64.10% of Python online submissions for Sort Colors.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        start = 0
        end = n-1
        
        i = 0
        while i < n and i <= end :
            
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                i += 1
            
            elif nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            
            else:
                i += 1