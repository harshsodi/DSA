# Runtime: 4304 ms, faster than 30.30% of Python online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 33.9 MB, less than 11.11% of Python online submissions for Maximum Length of Repeated Subarray.

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        m = len(A)
        n = len(B)
        
        dp = [[0 for _ in range(n)] for x in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                        ans = max(ans, dp[i][j])
        
        return ans