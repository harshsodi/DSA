# Runtime: 92 ms, faster than 86.54% of Python online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for The K Weakest Rows in a Matrix.

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        m = len(mat)
        if m == 0:
            return []
        n = len(mat[0])
        
        def bs(arr):
            l = 0
            r = len(arr) - 1
            
            while l < r:
                mid = (l+r)/2
                if arr[mid] == 1:
                    l = mid+1
                else:
                    r = mid
            
            if arr[l] == 1:
                return l
            else:
                return l-1
        
        def fs(e1, e2):
            if e1[0] < e2[0]:
                return -1
            elif e1[0] > e2[0]:
                return 1
            else:
                if e1[1] < e2[1]:
                    return -1
                else:
                    return 1
        
        a = []
        for i in range(m):
            a.append([bs(mat[i]), i])
        
        a = sorted(a, cmp=lambda x,y: fs(x, y))
        return [u[1] for u in a][:k]