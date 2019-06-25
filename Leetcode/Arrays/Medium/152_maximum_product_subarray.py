# Runtime: 32 ms, faster than 94.93% of Python online submissions for Maximum Product Subarray.
# Memory Usage: 12 MB, less than 88.37% of Python online submissions for Maximum Product Subarray.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        size = len(nums)
        
        max_prod = nums[0]
        local1 = 1
        local2 = 1
        visited = False
        
        for i in range(size):
            
            local1 *= nums[i]
            max_prod = max(max_prod, local1)
            
            if nums[i] == 0:
                local1 = 1
                local2 = 1
                visited = False
            
            if visited:
                local2 *= nums[i]
                max_prod = max(max_prod, local2)
            elif(nums[i] < 0):
                visited = True
                        
        return max_prod