# Runtime: 40 ms, faster than 89.80% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        nums_ = sorted(nums)
        
        d = {}
        for i in range(n):
            if d.get(nums_[i]) == None:
                d[nums_[i]] = i
        
        return [d[i] for i in nums]