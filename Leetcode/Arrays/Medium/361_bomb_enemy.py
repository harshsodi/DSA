# Your submission beats 65.20% Submissions!

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        tar = [[0 for i in range(n)] for _ in range(m)]
        
        for i in range(m):
            e = 0
            for j in range(n):
                
                if grid[i][j] == 'W':
                    e = 0
                if grid[i][j] == 'E':
                    e += 1
                    continue
            
                tar[i][j] += e
            
            e = 0
            
            j = n-1
            while j >= 0:
                if grid[i][j] == 'W':
                    e = 0
                    tar[i][j] = -1
                if grid[i][j] == 'E':
                    e += 1
                    tar[i][j] = -1
                    j -= 1
                    continue
            
                tar[i][j] += e
                j -= 1
    
        for i in range(n):
            e = 0
            for j in range(m):
                
                if grid[j][i] == 'W':
                    e = 0
                if grid[j][i] == 'E':
                    e += 1
                    continue
            
                tar[j][i] += e
            
            e = 0
            
            j = m-1
            while j >= 0:
                if grid[j][i] == 'W':
                    e = 0
                    tar[j][i] = -1
                if grid[j][i] == 'E':
                    e += 1
                    tar[j][i] = -1
                    j -= 1
                    continue
            
                tar[j][i] += e
                j -= 1
        
        ans = 0
        for i in tar:
            for j in i:
                ans = max(ans, j)
            print
    
        return ans