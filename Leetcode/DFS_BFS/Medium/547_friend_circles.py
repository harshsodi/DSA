# Runtime: 180 ms, faster than 58.49% of Python online submissions for Friend Circles.
# Memory Usage: 12.3 MB, less than 22.22% of Python online submissions for Friend Circles.

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        n = len(M)
        mem = {}
        
        def f(root):
            if mem.get(root):
                return
            
            mem[root] = True
            
            for ch in range(n):
                if M[root][ch]:
                    f(ch)
    
        ans = 0
        for i in range(n):
            if mem.get(i) == None:
                ans += 1
                f(i)
        
        return ans