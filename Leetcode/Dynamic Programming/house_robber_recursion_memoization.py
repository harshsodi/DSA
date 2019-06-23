# Runtime: 8 ms, faster than 99.77% of Python online submissions for House Robber.
# Memory Usage: 11.7 MB, less than 56.67% of Python online submissions for House Robber.

class Solution(object):

    def solve(self, nums, end, x):
        
        if self.memo.get(end) != None:
            return self.memo[end]

        l = len(nums)

        if end >= l:    
            return 0

        if end+2 < l:
            p1 = self.solve(nums, end+2, x)
            p2 = self.solve(nums, end+3, x)
            self.memo[end] = nums[end] + max(p1, p2)
            return self.memo[end]
        else:
            self.memo[end] = nums[end]
            return nums[end]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        l = len(nums)
        
        self.memo = {}
    
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0], nums[1])
    
        return max(self.solve(nums, 0, nums[0]), self.solve(nums, 1, nums[1]))