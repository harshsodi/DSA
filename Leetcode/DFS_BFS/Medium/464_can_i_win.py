class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        arr = [x for x in range(1, maxChoosableInteger + 1)]
        mem = {}
        
        def f(rem, nums):
            
            if mem.get((rem, tuple(nums))) != None:
                return mem[(rem, tuple(nums))]
                
            if rem <= 0:
                return False
            
            for i in range(len(nums)):
                use = nums[i]
                if f(rem - use, nums[:i] + nums[i+1:]) == False:
                    mem[(rem, tuple(nums))] = True
                    return True
            
            mem[(rem, tuple(nums))] = False
            return False
    
        if desiredTotal <= maxChoosableInteger:
            return True
    
        mx = maxChoosableInteger * (maxChoosableInteger+1)/2
        if mx < desiredTotal:
            return False
    
        return f(desiredTotal, arr)