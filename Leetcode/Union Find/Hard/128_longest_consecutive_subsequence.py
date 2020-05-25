# Runtime: 68 ms, faster than 21.51% of Python online submissions for Longest Consecutive Sequence.
# Memory Usage: 14.1 MB, less than 5.00% of Python online submissions for Longest Consecutive Sequence.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        class DSU:
            def __init__(self, n):
                self.p = range(n)
                
            def find(self, u):
                if self.p[u] == u:
                    return u

                self.p[u] = self.find(self.p[u])
                return self.p[u]

            def union(self, u, v):
                self.p[self.find(u)] = self.find(v)
        
            def get_map(self):
                return self.p
        
        n = len(nums)
        mem = {}
        d = {}
        
        dsu = DSU(n)
        
        for i in range(n):
            num = nums[i]
            if mem.get(num) != None:
                continue
            
            mem[num] = i
            if mem.get(num+1) != None:
                dsu.union(i, mem[num+1])
            
            if mem.get(num-1) != None:
                dsu.union(mem[num-1], i)
        
        d = {}
        ans = 0
        
        for i in range(n):
            par = dsu.find(i)
            d[par] = d.get(par, 0) + 1
            ans = max(ans, d[par])
        
        return ans