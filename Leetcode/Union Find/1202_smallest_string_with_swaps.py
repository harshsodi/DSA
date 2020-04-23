# Runtime: 704 ms, faster than 80.39% of Python online submissions for Smallest String With Swaps.
# Memory Usage: 50.8 MB, less than 100.00% of Python online submissions for Smallest String With Swaps.

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
        s = [i for i in s]
        
        n = len(s)
        parents = [i for i in range(n)]
    
        def find(u):
            if parents[u] == u:
                return u
        
            parents[u] = find(parents[u])
            return parents[u]
    
        def union(u, v):
            upar = find(u)
            vpar = find(v)
                        
            if upar != vpar:
                parents[upar] = vpar
        
        for i in pairs:
            u = i[0]
            v = i[1]
            
            union(u, v)
        
        # print parents
        
        mem = defaultdict(list)
        
        for i in range(n):
            pi = find(i)
            if mem.get(pi) == None:
                mem[pi] = []
            mem[pi].append(i)
    
        # print mem
    
        for k in mem:
            v = sorted(mem[k])
            st = sorted([s[ch] for ch in v])
            
            for j in range(len(v)):
                s[v[j]] = st[j] 
        
        return "".join(s)