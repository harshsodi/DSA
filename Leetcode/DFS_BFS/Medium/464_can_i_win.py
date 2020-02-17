# Runtime: 1308 ms, faster than 20.00% of Python online submissions for Can I Win.
# Memory Usage: 34.9 MB, less than 100.00% of Python online submissions for Can I Win.

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        arr = [x for x in range(1, maxChoosableInteger + 1)]
        mem = {}
        
        def f(rem, nums, t):
            
            if mem.get((tuple(nums), rem, t)) != None:
                return mem[(tuple(nums), rem, t)]
            
            if rem <= 0:
                if t == 1:
                    return True
                else:
                    return False
            
            if nums == []:
                return False
            
            win = False
            if t == 1:
                win = True
            
            for i in range(len(nums)):
                touse = nums[i] 
                
                verd = f(rem - touse, nums[:i] + nums[i+1:], 1-t)
                if t == 0 and verd == True:
                    win = True
                    break
                
                if t == 1 and verd == False:
                    win = False
                    break
                    
            mem[(tuple(nums), rem, t)] = win
            return win
    
        if desiredTotal <= maxChoosableInteger:
            return True
    
        return f(desiredTotal, arr, 0)