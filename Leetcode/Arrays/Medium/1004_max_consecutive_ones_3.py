# Runtime: 632 ms, faster than 12.66% of Python online submissions for Max Consecutive Ones III.
# Memory Usage: 12 MB, less than 100.00% of Python online submissions for Max Consecutive Ones III.

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        n = len(A)
        
        if n == 0:
            return 0
        
        ans = 0
        l = 0
        r = 0
        z = 0
        
        if A[0] == 0:
            z = 1
            if K > 0:
                ans = 1
        
        while l < n-1:
            while r < n-1:
                r += 1
                
                if A[r] == 0:
                    z += 1
                
                if z > K:
                    break
                else:
                    ans = max(ans, r-l+1)
            
            while l < r:
                if A[l] == 0:
                    z -= 1
                
                l += 1
                
                if z <= K:
                    break
                
        return ans