# Runtime: 216 ms, faster than 57.96% of Python online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 24.1 MB, less than 100.00% of Python online submissions for Number of Equivalent Domino Pairs.

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        
        d = {}
        for i in dominoes:
            mn = min(i[0],i[1])
            mx = max(i[0],i[1])
            domino = (mn, mx)
            d[domino] = d.get(domino,0) + 1
        
        ans = 0
        for i in d:
            ans += d[i] * (d[i] - 1) / 2
            
        return ans