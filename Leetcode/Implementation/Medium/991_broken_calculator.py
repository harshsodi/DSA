# Runtime: 12 ms, faster than 90.03% of Python online submissions for Broken Calculator
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Broken Calculator.

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        
        steps = 0
        
        if Y < X:
            return abs(Y-X)
        
        while Y != X:
            if Y % 2:
                Y += 1
                steps += 1
            else:
                if X <= Y/2:
                    Y /= 2
                    steps += 1
                else:
                    steps += min(1 + abs(Y/2 - X), abs(Y - X*2) + 1)
                    break

        return steps