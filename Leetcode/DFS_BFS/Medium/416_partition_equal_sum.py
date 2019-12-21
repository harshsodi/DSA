# Runtime: 84 ms, faster than 74.04% of Python online submissions for Partition Equal Subset Sum.
# Memory Usage: 11.8 MB, less than 87.50% of Python online submissions for Partition Equal Subset Sum.

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def f(path, path_sum, nums, n, t):
            
            if self.ans == True:
                return
            
            for i in range(path[-1]+1, n):
                new_path = path + [i]
                new_path_sum = path_sum + nums[i]
                
                if new_path_sum == t:
                    self.ans = True
                    return
            
                if new_path_sum > t:
                    return
                
                f(new_path, new_path_sum, nums, n, t)
        
        n = len(nums)
        if n <= 1:
            return False
        
        s = 0
        for i in nums:
            s += i
        
        if s%2 != 0:
            return False
        
        t = s/2
            
        self.ans = False
        
        f([-1], 0, list(sorted(nums, reverse=True)), n, t)
        return self.ans