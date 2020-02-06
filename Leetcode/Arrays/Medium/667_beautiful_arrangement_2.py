# Runtime: 36 ms, faster than 76.09% of Python online submissions for Beautiful Arrangement II.
# Memory Usage: 12.7 MB, less than 50.00% of Python online submissions for Beautiful Arrangement II.

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
        t = k + 1
        
        ans = []
        for i in range(1, t/2+1):
            ans.append(i)
            ans.append(t-i+1)
        
        if t%2:
            ans.append(t/2+1)
        
        for i in range(t+1, n+1):
            ans.append(i)
        
        return ans