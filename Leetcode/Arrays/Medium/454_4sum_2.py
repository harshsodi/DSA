# Runtime: 524 ms, faster than 7.58% of Python online submissions for 4Sum II.
# Memory Usage: 53.6 MB, less than 12.50% of Python online submissions for 4Sum II.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        n = len(A)
        
        ab = {}
        cd = {}
        
        for i in range(n):
            for j in range(n):
                ab[A[i] + B[j]] = ab.get(A[i] + B[j], 0) + 1
        
        for i in range(n):
            for j in range(n):
                cd[C[i] + D[j]] = cd.get(C[i] + D[j], 0) + 1

        cdk = cd.keys()
        
        ans = 0
        
        for i in cdk:
            
            x = cd.get(i)
            y = ab.get(-1*i, 0)
            
            ans += x*y
    
        return ans