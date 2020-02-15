# Runtime: 232 ms, faster than 45.73% of Python online submissions for Minimum Height Trees.
# Memory Usage: 16.1 MB, less than 66.67% of Python online submissions for Minimum Height Trees.

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # DFS from all ndoes ..!? No fucking way
        
        if n == 1:
            return [0]
    
        if n == 2:
            return edges[0]
        
        g = {}
        ne = {}
        leaves = []
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            if g.get(u) == None:
                g[u] = []
            if g.get(v) == None:
                g[v] = []
            
            g[u].append(v)
            g[v].append(u)
        
        for vert in range(n):
            if len(g[vert]) == 1:
                leaves.append(vert)
          
        while n > 2:
            nxt_level = []
            n = n - len(leaves)
            
            for i in leaves:    
                ch = g[i].pop()
                g[ch].remove(i)    
                if len(g[ch]) == 1:
                    nxt_level.append(ch)
            
            leaves = nxt_level
            
        return leaves