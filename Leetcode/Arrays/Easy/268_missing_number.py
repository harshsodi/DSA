# Runtime: 120 ms, faster than 92.03% of Python online submissions for Missing Number.
# Memory Usage: 12.9 MB, less than 21.05% of Python online submissions for Missing Number.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        
        sum_that_is = reduce(lambda x,y: x+y, nums)
        sum_that_should_be = l * (l+1)/2
    
        return sum_that_should_be - sum_that_is
        