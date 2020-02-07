# Runtime: 836 ms, faster than 40.20% of Python online submissions for Cherry Pickup.
# Memory Usage: 51.4 MB, less than 100.00% of Python online submissions for Cherry Pickup.

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        
        mem = {}
        
        def f(ax, ay, bx):
            by = ax+ay-bx
            
            if mem.get((ax,ay,bx)):
                return mem[(ax,ay,bx)]

            if ax >= n or ay >= n or bx >= n or by >= n:
                return float('-inf')
            
            if grid[ax][ay] == -1 or grid[bx][by] == -1:
                return float('-inf')
            
            if ax == n-1 and ay == n-1:
                return grid[n-1][n-1]
            
            ac = 0
            bc = 0
            
            if grid[ax][ay] == 1:
                ac = 1
            if grid[bx][by] == 1 and (bx != ax and by != ay):
                bc = 1
            
            total_c = ac + bc
            
            m = max([
                f(ax+1, ay, bx),
                f(ax+1, ay, bx+1),
                f(ax, ay+1, bx),
                f(ax, ay+1, bx+1)
            ])
            
            mem[(ax,ay,bx)] = total_c + m
            return total_c + m
        
        ans = f(0,0,0)
        return max(0, ans) 