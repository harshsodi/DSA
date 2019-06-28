# Runtime: 16 ms, faster than 95.22% of Python online submissions for Subsets.
# Memory Usage: 11.7 MB, less than 90.88% of Python online submissions for Subsets.

class Solution(object):
    
    def make(self, curr, nums, start):
        
        size = len(nums)
    
        self.power_set.append(copy.deepcopy(curr))
        
        for i in range(start, size):
            curr.append(nums[i])
            self.make(curr, nums, i+1)
            curr.pop(len(curr) - 1)
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.power_set = []
        self.make([], nums, 0)
        
        return self.power_set