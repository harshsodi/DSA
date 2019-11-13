# Runtime: 448 ms, faster than 82.96% of Python online submissions for Island Perimeter.
# Memory Usage: 12 MB, less than 70.59% of Python online submissions for Island Perimeter.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        if m == 0:
            return 0
    
        n = len(grid[0])
                
        perm = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                
                    if i == 0:
                        perm += 1
                    if i == m-1:
                        perm += 1
                    if i > 0 and grid[i-1][j] == 0:
                        perm += 1
                    if i<m-1 and grid[i+1][j] == 0:
                        perm += 1

                    if j == 0:
                        perm += 1
                    if j == n-1:
                        perm += 1
                    if j > 0 and grid[i][j-1] == 0:
                        perm += 1
                    if j<n-1 and grid[i][j+1] == 0:
                        perm += 1
        
        return perm