# Runtime: 60 ms, faster than 23.59% of Python online submissions for Redundant Connection.
# Memory Usage: 13.1 MB, less than 25.00% of Python online submissions for Redundant Connection.

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(edges)
        g = {}
        mem = {}
        
        def f(source, dest):
            
            if mem.get(source) != None:
                return False
            
            mem[source] = True
            
            if source == dest:
                return True
            else:
                for child in g.get(source, []):
                    if f(child, dest):
                        return True
                return False
        
        seen = {}
        
        for edge in edges:
            
            u = edge[0]
            v = edge[1]
        
            mem = {}
            if seen.get(u) and seen.get(v) and f(u, v):
                return edge
            
            seen[u] = True
            seen[v] = True
            
            if g.get(u) == None:
                g[u] = []
                
            if g.get(edge[1]) == None:
                g[v] = []
            
            g[u].append(v)
            g[v].append(u)