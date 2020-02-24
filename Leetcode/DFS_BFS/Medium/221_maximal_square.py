# Runtime: 344 ms, faster than 11.48% of Python online submissions for Maximal Square.
# Memory Usage: 31.5 MB, less than 12.50% of Python online submissions for Maximal Square.

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
    
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
    
        
        mem = {}
        mvs = [[1,0],[0,1],[1,1]]
        ans = {1: 0}
    
        def f(i, j):
            
            if mem.get((i, j)) != None:
                return mem[(i, j)]
            
            if i == m or j == n:
                return 0
            
            ans[1] = max(ans[1], int(matrix[i][j]))
            
            a1 = f(i+1,j+1)
            a2 = f(i, j+1)
            a3 = f(i+1, j)
            
            a = (min([a1, a2, a3]) + 1) * int(matrix[i][j])
            mem[(i, j)] = a
            ans[1] = max(ans[1], a)
            
            # print "(", i, j, ")", a
            
            return a
    
        f(0,0)
        return ans[1] * ans[1]