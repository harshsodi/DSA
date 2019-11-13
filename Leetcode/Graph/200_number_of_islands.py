# Runtime: 128 ms, faster than 72.77% of Python online submissions for Number of Islands.
# Memory Usage: 19 MB, less than 55.40% of Python online submissions for Number of Islands.

class Solution(object):
    
    def isvalid(self, i, j, m, n):
        return i >= 0 and j >= 0 and i<m and j<n
        
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
    
        if m == 0 or n == 0:
            return 0
    
        ans = 0
    
        for i in range(m):
            for j in range(n):
            
                if grid[i][j] == "1":    
                    
                    ans += 1
                    
                    q = [(i,j)]
                    
                    while len(q):
                        t = q.pop(0)
                        
                        grid[t[0]][t[1]] = "0"
                        
                        upx, upy = t[0]-1, t[1]
                        downx, downy = t[0]+1, t[1]
                        leftx, lefty = t[0], t[1]-1
                        rightx, righty = t[0], t[1]+1
        
                        if self.isvalid(upx, upy, m, n) and grid[upx][upy] == "1":
                            q.append((upx, upy))
                            grid[upx][upy] = "0"
                    
                        if self.isvalid(downx, downy, m, n) and grid[downx][downy] == "1":
                            q.append((downx, downy))
                            grid[downx][downy] = "0"
                            
                        if self.isvalid(leftx, lefty, m, n) and grid[leftx][lefty] == "1":
                            q.append((leftx, lefty))
                            grid[leftx][lefty] = "0"
                            
                        if self.isvalid(rightx, righty, m, n) and grid[rightx][righty] == "1":
                            q.append((rightx, righty))
                            grid[rightx][righty] = "0"
        
        return ans