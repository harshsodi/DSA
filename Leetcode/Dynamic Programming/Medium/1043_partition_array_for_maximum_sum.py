# Runtime: 448 ms, faster than 41.60% of Python online submissions for Partition Array for Maximum Sum.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Partition Array for Maximum Sum.

class Solution(object):

    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        n = len(A)
        
        dp = [0 for _ in A]
        dp[0] = A[0]
        
        for i in range(1, n):
            cmax = A[i]
            for j in range(0, K):
                c = i - j
                if c < 0:
                    break
                
                if c == 0:
                    prev = 0
                else:
                    prev = dp[c-1]
                
                cmax = max(cmax, A[c])
                dp[i] = max(dp[i], cmax * (j+1) + prev)
                
        return dp[n-1]