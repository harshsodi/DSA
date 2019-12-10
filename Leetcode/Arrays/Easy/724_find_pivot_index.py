# Runtime: 152 ms, faster than 12.31% of Python online submissions for Find Pivot Index.
# Memory Usage: 12.8 MB, less than 10.00% of Python online submissions for Find Pivot Index.

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        r = [_ for _ in nums]
                
        for i in range(1,n):
            j = n - i - 1
            r[j] = r[j+1] + r[j]
    
        s = 0
        for i in range(0,n):
            s += nums[i]
            
            if s == r[i]:
                return i
        
        return -1