# Runtime: 32 ms, faster than 58.51% of Python online submissions for Interleaving String.
# Memory Usage: 13.1 MB, less than 7.88% of Python online submissions for Interleaving String.

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        self.n = len(s1) + len(s2)
        
        if self.n != len(s3):
            return False
        
        self.mem = {}
        
        def f(i, j, st):
            
            if st != s3[: len(st)]:
                return False
            
            if self.mem.get((i, j, st)) != None:
                return self.mem[(i,j,st)]
            
            # print st
            
            if st == s3:
                return True
    
            if i >= len(s1) and j >= len(s2):
                return False
    
            if len(st) == self.n:
                return False
    
            a = False
            b = False
    
            if i < len(s1):
                a = f(i+1, j, st+s1[i])
            
            if j < len(s2):
                b = f(i, j+1, st + s2[j])

            self.mem[(i,j,st)] = a or b
            return self.mem[(i, j, st)]
            
        return f(0, 0, "")