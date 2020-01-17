# Runtime: 4 ms, faster than 100.00% of Python online submissions for Find N Unique Integers Sum up to Zero.
# Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Find N Unique Integers Sum up to Zero.

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        ans = [0 for _ in range(n)]
        if n%2 == 1:
            ans[n/2] = 0
        
        l = 0
        r = n-1
        
        i = 1
        
        while l < r:
            ans[l] = i
            ans[r] = -i
            i += 1
            
            l += 1
            r -= 1
        
        return ans