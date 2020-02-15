# Runtime: 136 ms, faster than 23.96% of Python online submissions for Course Schedule.
# Memory Usage: 30.6 MB, less than 5.09% of Python online submissions for Course Schedule.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
    
        n = len(prerequisites)
    
        g = [[] for _ in range(numCourses+1)]
    
        for edge in prerequisites:
            u = edge[0]
            v = edge[1]
            
            g[u].append(v)
    
        mem = {}
        
        def f(root, path):
            
            if mem.get(root):
                return mem[root]
            
            if root in path:
                return False
            
            valid = True
            
            for child in g[root]:
                ret = f(child, path+[root])
                
                if ret == False:
                    valid = False
                    break
            
            mem[root] = valid
            return valid
    
        for i in range(numCourses):
                        
            if not f(i, []):
                return False
        
        return True