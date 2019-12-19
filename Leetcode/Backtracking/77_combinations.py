# Runtime: 612 ms, faster than 58.71% of Python online submissions for Combinations.
# Memory Usage: 13.1 MB, less than 69.23% of Python online submissions for Combinations.

class Solution(object):
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        def f(n, k, c, ls):
            if len(ls) == k:
                self.ans.append(ls)
                return

            for i in range(c+1, n+1):
                f(n, k, i, ls+[i])    
        
        self.ans = []
        
        for i in range(1, n-k+2):
            f(n, k, i, [i])
        
        return self.ans