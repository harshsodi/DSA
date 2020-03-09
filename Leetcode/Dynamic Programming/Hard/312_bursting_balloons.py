# Runtime: 928 ms, faster than 15.16% of Python online submissions for Burst Balloons.
# Memory Usage: 14.7 MB, less than 14.29% of Python online submissions for Burst Balloons.

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = [1] + nums + [1]
        n = len(nums)
        
        mem = {}
        
        def f(i, j):
            
            if mem.get((i, j)) != None:
                return mem[(i,j)]
            
            ans = 0
                    
            for k in range(i+1, j):
                ans = max(ans, nums[i] * nums[k] * nums[j] + f(i, k) + f(k, j))    
    
            mem[(i, j)] = ans
            return ans
    
        return f(0, n-1)