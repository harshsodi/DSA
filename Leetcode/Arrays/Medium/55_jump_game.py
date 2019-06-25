# Runtime: 84 ms, faster than 35.55% of Python online submissions for Jump Game.
# Memory Usage: 13.5 MB, less than 10.76% of Python online submissions for Jump Game.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        size = len(nums)
        if size == 1:
            return True
        
        i = size - 1
        f = False
        
        while i > 0:
            i -= 1
            d = 1
            f = False
            
            while i >= 0:
                if nums[i] >=d:
                    f = True
                    break
                else:
                    d += 1
                    i -= 1
            
            if not f:
                break
        
        if not f:
            return False
        else :
            return True