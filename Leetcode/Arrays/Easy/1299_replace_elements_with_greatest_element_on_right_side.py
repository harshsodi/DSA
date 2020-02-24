# Runtime: 116 ms, faster than 40.83% of Python online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 13.4 MB, less than 100.00% of Python online submissions for Replace Elements with Greatest Element on Right Side.

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        n = len(arr)
        
        ans = [None for _ in range(n)]
        ans[n-1] = -1

        i = n-2
        while i >= 0:
            ans[i] = max(ans[i+1], arr[i+1])
            i -= 1
        
        return ans