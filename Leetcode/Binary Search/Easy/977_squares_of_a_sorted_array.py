# Runtime: 208 ms, faster than 56.98% of Python online submissions for Squares of a Sorted Array.
# Memory Usage: 13.9 MB, less than 20.51% of Python online submissions for Squares of a Sorted Array.

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        n = len(A)
        
        # Binary Search for 1st positive number
        l = 0
        r = n-1
        
        m = None
        while l < r:
            m = (l+r)/2
            if A[m] < 0:
                l += 1
            else:
                r = m
        
        i = l
        j = l-1
        
        ans = []
        
        while i < n and j >= 0:
            a = A[i]*A[i]
            b = A[j]*A[j]
            
            if a > b:
                ans.append(b)
                j -= 1
            else:
                ans.append(a)
                i += 1
        
        while i < n:
            ans.append(A[i]*A[i])
            i += 1
        
        while j >= 0:
            ans.append(A[j]*A[j])
            j -= 1
        
        return ans