# Runtime: 12 ms, faster than 93.46% of Python online submissions for Max Chunks To Make Sorted.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Max Chunks To Make Sorted.

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        max_yet = float('-inf')
        
        ans = 0
        
        for i in range(n):
            
            max_yet = max(max_yet, arr[i])
            
            if i == max_yet:
                ans += 1
        
        return ans        