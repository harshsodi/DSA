# Your submission beats 94.80% Submissions!

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
    
        if n == 1:
            return True
    
        if len(edges) == 0:
            return False
        
        if len(edges) < n-1:
            return False
    
        g = [[] for _ in range(n)]
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            g[u].append(v)
            g[v].append(u)
        
        root = edges[0][0]
        vedges = {}
        vnodes = {root:True}
        ans = {"ans":True}
        
        def f(root):
            
            # print "Visiting", root
            
            if ans["ans"] == False:
                return False
            
            for ch in g[root]:
                
                if vedges.get((root,ch)) != None:
                    continue
                
                if vnodes.get(ch) != None:
                    ans["ans"] = False
                    # print "Falsing"
                    return False
                
                vnodes[ch] = True
                vedges[(root, ch)] = True
                vedges[(ch, root)] = True
                
                if not f(ch):
                    break
            
            return True
        
        f(root)
        
        if not ans["ans"]:
            return False
        
        
        if len(vnodes) < n:
            return False
        
        return True