# Runtime: 556 ms, faster than 51.91% of Python online submissions for Longest Arithmetic Subsequence of Given Difference.
# Memory Usage: 23.1 MB, less than 100.00% of Python online submissions for Longest Arithmetic Subsequence of Given

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        
        d = {}
        maxi = 0
        
        for c in arr:
            f = c - difference
            
            d[c] = d.get(f,0) + 1
            maxi = max(maxi, d[c])
        
        return maxi