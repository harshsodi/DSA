# Runtime: 16 ms, faster than 82.40% of Python online submissions for House Robber II.
# Memory Usage: 11.8 MB, less than 44.44% of Python online submissions for House Robber II.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], max(nums[1], nums[2]))
    
        dp1 = [0 for _ in range(n-1)]
        dp2 = [0 for _ in range(n)]
        
        dp1[0] = nums[0]
        dp1[1] = nums[1]
        dp1[2] = nums[2] + nums[0]
        
        dp2[1] = nums[1]
        dp2[2] = nums[2]
        dp2[3] = nums[3] + nums[1]
        
        for i in range(3, n-1):
            dp1[i] = max(max(dp1[i-2] + nums[i], dp1[i-3] + nums[i]), dp1[i-1])
            
        for i in range(4, n):
            dp2[i] = max(dp2[i-1], max(dp2[i-2] + nums[i], dp2[i-3] + nums[i]))
        
        print dp1
        print dp2
        
        return max(dp1[-1], dp2[-1])