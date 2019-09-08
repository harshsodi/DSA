# Runtime: 16 ms, faster than 66.67% of Python online submissions for Climbing Stairs.
# Memory Usage: 11.5 MB, less than 82.81% of Python online submissions for Climbing Stairs.

class Solution(object):
    
    def no_ways(self, target):
    
        l = target
        arr = [0 for _ in range(l+1)]
        
        arr[target] = 1
        arr[target-1] = 1
        
        curr = target - 2
        
        while curr > -1:
            arr[curr] = arr[curr+1] + arr[curr+2]
            curr -= 1
    
        # print arr
        return arr[0]
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.memo = {}
        
        return self.no_ways(n)