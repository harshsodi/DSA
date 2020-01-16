# Runtime: 1172 ms, faster than 35.71% of Python online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 13 MB, less than 100.00% of Python online submissions for Minimum Domino Rotations For Equal Row.

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        n = len(A)
        
        a_possible = True
        b_possible = True
        
        a = A[0]
        b = B[0]
        
        ad = {}
        bd = {}
        
        for i in range(n):
            
            if A[i] != B[i]:
                ad[A[i]] = ad.get(A[i], 0) + 1
                bd[B[i]] = bd.get(B[i], 0) + 1
            
            if A[i] != a and B[i] != a:
                a_possible = False
            
            if A[i] != b and B[i] != b:
                b_possible = False
        
        if a_possible and b_possible:
            return min([ad.get(a, 0), ad.get(b, 0), bd.get(a, 0), bd.get(b, 0)])
    
        if a_possible:
            return min(ad.get(a, 0), bd.get(a, 0))
        
        if b_possible:
            return min(ad.get(b, 0), bd.get(b, 0))
        
        if not a_possible and not b_possible:
            return -1