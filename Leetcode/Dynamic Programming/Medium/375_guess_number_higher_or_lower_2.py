# Runtime: 1400 ms, faster than 21.57% of Python online submissions for Guess Number Higher or Lower II.
# Memory Usage: 16.3 MB, less than 100.00% of Python online submissions for Guess Number Higher or Lower II.

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        mem = {}
        
        def f(l, r):
            
            if l >= r:
                return 0
            
            gmin = float('inf')
            for i in range(l, r+1):
                
                if mem.get((l, i-1)) == None:
                    lft = f(l, i-1)
                    mem[(l,i-1)] = lft
                else:
                    lft = mem[(l, i-1)]
                
                if mem.get((i+1,r)) == None:
                    rgt = f(i+1,r)
                    mem[(i+1,r)] = rgt
                else:
                    rgt = mem[(i+1,r)]
                
                lmax = i + max(lft, rgt)
                gmin = min(gmin, lmax)
        
            return gmin

        return f(1, n)