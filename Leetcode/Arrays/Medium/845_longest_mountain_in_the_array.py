# Runtime: 144 ms, faster than 87.16% of Python online submissions for Longest Mountain in Array.
# Memory Usage: 12.4 MB, less than 50.00% of Python online submissions for Longest Mountain in Array.

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        if n <= 2:
            return 0
        
        maxm = 0
        base = 0
        
        while base < n:
            
            step = base 
            
            # If at base climb
            if step+1 < n and A[step] < A[step+1]:
                while step+1 < n and A[step] < A[step+1]:
                    step += 1
                
                if step+1 < n and A[step] > A[step+1]:
                    while step+1 < n and A[step] > A[step+1]:
                        step += 1
                
                    maxm = max(step - base + 1, maxm)
            
                base = step
                
            else:
                # Walk on ground
                base += 1
                
        return maxm