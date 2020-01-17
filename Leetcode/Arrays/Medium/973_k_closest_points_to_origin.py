# Runtime: 624 ms, faster than 54.31% of Python online submissions for K Closest Points to Origin.
# Memory Usage: 17.6 MB, less than 60.38% of Python online submissions for K Closest Points to Origin.

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        def e(point):
            return point[0]*point[0] + point[1]*point[1]
        
        dst = [[e(x), x] for x in points]
        
        n = len(dst)
        
        l = 0
        r = n-1
        
        while True:
            i = l
            j = r
            
            p = r
            
            while i < j:
                while i < j and dst[i][0] <= dst[p][0]:
                    i += 1
                while i < j and dst[j][0] >= dst[p][0]:
                    j -= 1
                
                dst[i], dst[j] = dst[j], dst[i]
            
            if dst[i][0] > dst[p][0]:
                dst[i], dst[p] = dst[p], dst[j]
            
            pos = i
            
            if pos < K-1:
                l = pos + 1
            elif pos > K-1:
                r = pos - 1
            else:
                return [x[1] for x in dst[:pos+1]]