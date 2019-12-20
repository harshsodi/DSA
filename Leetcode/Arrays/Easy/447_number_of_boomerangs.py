# Runtime: 1228 ms, faster than 9.36% of Python online submissions for Number of Boomerangs.
# Memory Usage: 16.8 MB, less than 16.67% of Python online submissions for Number of Boomerangs.

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)

        ans = 0        
        mem = [[0 for _ in range(n)] for x in range(n)]
 
        for i in range(n):
            s_point = points[i]
            d = {}
            
            for j in range(n):
                
                if i == j:
                    continue

                t_point = points[j]
                
                dist = None
                if mem[i][j] != 0:
                    dist = mem[i][j]
                else:
                    dist = math.sqrt(pow(abs(s_point[0] - t_point[0]), 2) + pow(abs(s_point[1] - t_point[1]), 2))
                    mem[i][j] = dist
                    mem[j][i] = dist 
                
                d[dist] = d.get(dist,0) + 1
            
            # print s_point
            
            for i in d:
                cnt = d[i]
                ans += cnt*(cnt-1)
        
        return ans