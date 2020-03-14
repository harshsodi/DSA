# Runtime: 20 ms, faster than 47.25% of Python online submissions for Evaluate Division.
# Memory Usage: 11.8 MB, less than 55.00% of Python online submissions for Evaluate Division.

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        n = len(equations)
        
        g = {}
        
        for i in range(n):
            eq = equations[i]
            val = values[i]
            
            u = eq[0]
            v = eq[1]
            
            g[u] = g.get(u, []) + [(v, val)]
            g[v] = g.get(v, []) + [(u, 1.0/val)]
            
        def dfs(root, target, prod):
            
            if mem.get(root) != None:
                return False
            mem[root] = True
        
            if g.get(root) == None:
                return False
        
            if root == target:
                return prod
        
            tans = False
            for ch in g.get(root, []):
                chname = ch[0]
                chval = ch[1]
                
                tans = dfs(chname, target, prod * chval)
                if tans != False:
                    return tans
                    
            return False
    
        ans = []
        for q in queries:
            root = q[0]
            target = q[1]
            
            mem = {}
            a = dfs(root, target, 1)
            if a != False:
                ans.append(a)
            else:
                ans.append(-1.0)
                
        return ans