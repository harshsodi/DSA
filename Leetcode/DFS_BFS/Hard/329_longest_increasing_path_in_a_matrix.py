# Runtime: 492 ms, faster than 46.25% of Python online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 16.8 MB, less than 11.11% of Python online submissions for Longest Increasing Path in a Matrix.

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        
        n = len(matrix[0])
        
        moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        def f(i, j):
            if mem.get((i,j)):
                return mem[(i,j)]
            
            h = 1
            for move in moves:
                x = i + move[0]
                y = j + move[1]
                
                if m>x>=0 and n>y>=0:
                    if matrix[x][y] < matrix[i][j]:
                        h = max(h, f(x,y) + 1)
            mem[(i,j)] = h
            return h
    
        mem = {}
        
        ans = 1
        for j in range(m):
            for k in range(n):
                ans = max(ans, f(j, k)) 
        
        return ans