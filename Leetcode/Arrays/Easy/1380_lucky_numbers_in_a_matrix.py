# Runtime: 140 ms, faster than 11.88% of Python online submissions for Lucky Numbers in a Matrix.
# Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Lucky Numbers in a Matrix.

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        
        r = [float('inf') for _ in range(m)]
        c = [float('-inf') for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                r[i] = min(r[i], matrix[i][j])
                c[j] = max(c[j], matrix[i][j])
        
        ans = []
        for i in range(m):
            for j in range(n):
                if r[i] == c[j] and matrix[i][j] == r[i]:
                    ans.append(r[i])
        
        return ans