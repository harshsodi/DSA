# Runtime: 24 ms, faster than 22.11% of Python online submissions for Robot Bounded In Circle.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Robot Bounded In Circle.

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        x = 0
        y = 0
        
        d = 0
        
        for i in instructions*4:
            if i == 'G':
                if d == 0:
                    y += 1
                if d == 1:
                    x += 1
                if d == 2: 
                    y -= 1
                if d == 3:
                    x -= 1
            
            if i == 'L':
                d = (d+1)%4
            elif i == 'R':
                d -= 1
                if d == -1:
                    d = 3
        
        if x == 0 and y == 0 and d == 0:
            return True
        else:
            return False