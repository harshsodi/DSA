# Runtime: 20 ms, faster than 44.29% of Python online submissions for Spiral Matrix.
# Memory Usage: 11.8 MB, less than 51.52% of Python online submissions for Spiral Matrix.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(matrix)
        if m == 0:
            return []
        
        if m == 1:
            return matrix[0]
        
        n = len(matrix[0])
        
        ans = []
        
        layer = 0
        for layer in range((min(m,n)-1)/2 + 1):
            right_lim = n-layer-1
            bottom_lim = m-layer-1
            
            top = range(layer, right_lim+1)
            right = range(layer+1, bottom_lim+1)
            bottom = list(reversed(range(layer+1, right_lim)))
            left = list(reversed(range(layer+1, bottom_lim+1)))
            
            for i in top:
                ans.append(matrix[layer][i])
            
            for i in right:
                ans.append(matrix[i][right_lim])
            
            for i in bottom:
                ans.append(matrix[bottom_lim][i])
            
            if right_lim != layer:
                for i in left:
                    ans.append(matrix[i][layer])
            
        return ans