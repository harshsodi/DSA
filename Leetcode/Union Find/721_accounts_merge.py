# Runtime: 268 ms, faster than 37.91% of Python online submissions for Accounts Merge.
# Memory Usage: 19.1 MB, less than 25.00% of Python online submissions for Accounts Merge.

class DSU:
    def __init__(self):
        self.p = range(10001)

    def find(self, u):
        if self.p[u] == u:
            return u

        self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, u, v):
        self.p[self.find(u)] = self.find(v)

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
         
        dsu = DSU()
        
        e2name = {}
        e2id = {}
        
        eid = 0
        
        for acc in accounts:
            name = acc[0]
            
            for i in range(1, len(acc)):
                email = acc[i]
                e2name[email] = name
                if e2id.get(email) == None:
                    e2id[email] = eid
                    eid += 1
                
                dsu.union(e2id[acc[1]], e2id[email])
        
        ans = defaultdict(list)
        for em in e2name:
            ans[dsu.find(e2id[em])].append(em)
        
        return [[e2name[a[0]]] + sorted(a) for a in ans.values()]