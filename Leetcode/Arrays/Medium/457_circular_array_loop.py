# Runtime: 392 ms, faster than 35.37% of Python online submissions for Circular Array Loop.
# Memory Usage: 11.7 MB, less than 50.00% of Python online submissions for Circular Array Loop.

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        v = {}
        
        for i in range(n):
            currnum = nums[i]
            way = currnum / abs(currnum)
            
            curri = i
                        
            l = 0
            while True:
              
                l += 1
                if l > n:
                    return True
                
                currway = currnum/abs(currnum)
                
                if currway == way:
                    nxti = (curri + currnum)%n
                    
                    if nxti == curri:
                        break
                    
                    curri = nxti
                    currnum = nums[curri]
                else:
                    break
        
        return False