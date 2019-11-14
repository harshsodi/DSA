# Runtime: 448 ms, faster than 20.41% of Python3 online submissions for Frog Jump.
# Memory Usage: 18.1 MB, less than 16.67% of Python3 online submissions for Frog Jump.

class Solution(object):
    
    def f(self, pos, step, arr):
            
        # print pos, step
        if self.memo.get((pos,step)):
            return False
        else:
            self.memo[(pos, step)] = True
            
        if pos == arr[-1]:
            return True
    
        if pos > arr[-1] or not self.positions.get(pos):
            return False
    
        if step > 1:
            x = self.f(pos+step-1, step-1, arr)
        else:
            x = False
        y = self.f(pos+step, step, arr)
        z = self.f(pos+step+1, step+1, arr)
        
        return  y or z or x 

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        # Create full track
        
        self.memo = {}
        self.positions = {}
        
        for i in stones:
            self.positions[i] = True
    
        return self.f(1, 1, stones)