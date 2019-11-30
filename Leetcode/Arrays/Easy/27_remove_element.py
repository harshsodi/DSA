# Runtime: 20 ms, faster than 64.67% of Python online submissions for Remove Element.
# Memory Usage: 11.8 MB, less than 35.85% of Python online submissions for Remove Element.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        n = len(nums)
        g = 0
        
        for i in range(n):
            if nums[i] == val:
                g += 1
                continue
        
            nums[i-g] = nums[i]
        
        ans = g
        
        while g > 0:
            nums.pop()
            g -= 1
        
        return n-ans
            