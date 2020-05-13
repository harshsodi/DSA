# Runtime: 896 ms, faster than 16.06% of Python online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 21.8 MB, less than 100.00% of Python online submissions for Number of Dice Rolls With Target Sum.

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        
        self.cap = pow(10, 9) + 7
        self.mem = {}
        
        def rec(s, d):
                        
            if self.mem.get((s,d)) != None:
                a = self.mem[(s,d)]
                return a % self.cap
                
            if s == 0 and d == 0:
                return 1
            
            if s < 0 or d < 0:
                return 0
            
            a = 0
            for i in range(1, f+1):
                a += rec(s-i, d-1)
                    
            self.mem[(s, d)] = a
            return a % self.cap
        
        return rec(target, d)