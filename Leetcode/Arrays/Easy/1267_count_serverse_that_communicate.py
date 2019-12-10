# Runtime: 456 ms, faster than 84.00% of Python online submissions for Count Servers that Communicate.
# Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Count Servers that Communicate.

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        r = [0 for _ in grid]
        c = [0 for _ in grid[0]]
        
        total_servers = 0
        
        for i in range(len(r)):
            for j in range(len(c)):
                if grid[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
                    total_servers += 1
        
        print total_servers
        print r
        print c
        
        minus = 0
        for i in range(len(r)):
            for j in range(len(c)):
                if grid[i][j] == 1 and r[i] == 1 and c[j] == 1:
                    minus += 1
        
        return total_servers - minus