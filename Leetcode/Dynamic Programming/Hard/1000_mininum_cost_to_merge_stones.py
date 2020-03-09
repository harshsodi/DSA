# Runtime: 40 ms, faster than 52.00% of Python online submissions for Minimum Cost to Merge Stones.
# Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Minimum Cost to Merge Stones.

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        
        n = len(stones)
        
        if (n-1) % (K-1) != 0:
            return -1
        
        ps = [0 for _ in stones] + [0]
        for i in range(0, n):
            ps[i+1] = ps[i] + stones[i]
        
        def get_sum(i, j):
            return ps[j+1] - ps[i]
        
        mem = {}
        
        def f(i, j):
            
            if i == j:
                return 0
            
            if mem.get((i, j)) != None:
                return mem[(i,j)]
            
            res = float('inf')
            
            p = i
            while p < j:
                res = min(res, f(i, p) + f(p+1, j))
                p += (K-1)
            
            if (j-i)%(K-1) == 0:
                res += get_sum(i, j)
            
            mem[(i,j)] = res
            return res
    
        return f(0, n-1)