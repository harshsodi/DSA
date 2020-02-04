# Runtime: 104 ms, faster than 24.30% of Python online submissions for Course Schedule II.
# Memory Usage: 15.5 MB, less than 5.55% of Python online submissions for Course Schedule II.

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        n = numCourses
        
        p = len(prerequisites)
        g = {}
        mem2 = {}
        
        def canReach(u, v):
            
            if mem2.get(u):
                return False
            
            mem2[u] = True
            
            if u == v:
                return True
            
            for c in g.get(u, []):
                if canReach(c, v):
                    return True
            return False
        
        for i in range(p):
            pq = prerequisites[i]
            u = pq[0]
            v = pq[1]
            
            mem2 = {}
            if canReach(v, u):
                return []
            
            if g.get(u) == None:
                g[u] = [v]
            else:
                g[u].append(v)
        
        # print g
        
        mem = {}
        
        def f(root):
            
            if mem.get(root):
                return []
            
            mem[root] = True
            
            if g.get(root, []) == []:
                return [root]
            
            a = []
            for c in g.get(root, []):
                a += f(c)
            
            return a + [root]
            
        ans = []
        
        for i in range(n):
            if mem.get(i):
                continue    
            else:
                ans += f(i)
        
        return ans