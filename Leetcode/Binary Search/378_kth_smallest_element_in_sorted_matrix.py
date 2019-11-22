# Runtime: 148 ms, faster than 90.57% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 17.2 MB, less than 65.22% of Python online submissions for Kth Smallest Element in a Sorted Matrix.

class Solution(object):
    
    def num_smaller(self, matrix, num):
        
        num_cols = len(matrix[0])
    
        ans = 0
        for row in matrix:
            l = 0
            r = num_cols-1
            
            while l<r:
                m = (l+r)/2
                if row[m] < num+1:
                    l = m+1
                else:
                    r = m
        
            if row[l] <= num:
                ans += l+1
            else:
                ans += l
        
        return ans  

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l<r:
            mid = (l+r)/2
            if self.num_smaller(matrix, mid) < k:
                l = mid+1
            else:
                r = mid
        
        return l