# Runtime: 632 ms, faster than 12.24% of Python online submissions for Maximum Sum Circular Subarray.
# Memory Usage: 16.5 MB, less than 50.00% of Python online submissions for Maximum Sum Circular Subarray.

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        
        curr_max = 0
        curr_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        total_sum = 0
        
        for i in range(n):
            nums = A[i]
            total_sum += nums
            
            curr_max = max(curr_max + A[i], A[i])
            curr_min = min(curr_min + A[i], A[i])
            
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
        
        max1 = max_sum
        max2 = total_sum - min_sum
        
        if max1 > 0:
            return max(max1, max2)
        else:
            return max1