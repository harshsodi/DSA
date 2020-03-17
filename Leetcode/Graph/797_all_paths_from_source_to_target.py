# Runtime: 92 ms, faster than 60.84% of Python online submissions for All Paths From Source to Target.
# Memory Usage: 13.2 MB, less than 33.33% of Python online submissions for All Paths From Source to Target.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(graph)
        
        def f(root, curr_path):
            
            if root == n-1:
                return [curr_path + [root]]
            
            paths = []
            for ch in graph[root]:
                paths += f(ch, curr_path + [root])
            
            return paths
    
        return f(0, [])