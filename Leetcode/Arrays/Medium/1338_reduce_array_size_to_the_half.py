# Runtime: 704 ms, faster than 47.58% of Python online submissions for Reduce Array Size to The Half.
# Memory Usage: 37.9 MB, less than 100.00% of Python online submissions for Reduce Array Size to The Half.
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        d = {}
        
        for i in arr:
            d[i] = d.get(i,0) + 1
        
        k = list(sorted([[x, d[x]] for x in d.keys()], key = lambda p: p[1], reverse=True))    
        # print k
        
        ans = 0
        s = 0
        i = 0
        while s < n/2:
            s += k[i][1]
            ans += 1
            i += 1
    
        return ans