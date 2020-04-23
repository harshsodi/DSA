# Runtime: 36 ms, faster than 95.70% of Python online submissions for Redundant Connection.
# Memory Usage: 13 MB, less than 25.00% of Python online submissions for Redundant Connection.

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(edges)
        p = [i for i in range(len(edges) + 1)]
        
        def ufind(u):
            if p[u] == u:
                return u
            
            p[u] = ufind(p[u])
            return p[u]
    
        def union(u, v):
            
            pu = ufind(u)
            pv = ufind(v)
            
            if pu != pv:
                p[pu] = pv
                return True
            else:
                return False
            
        for u, v in edges:
            
            if union(u, v) == False:
                return [u,v]