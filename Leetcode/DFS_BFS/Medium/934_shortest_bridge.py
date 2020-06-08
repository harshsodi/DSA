# Runtime: 744 ms, faster than 8.97% of Python online submissions for Shortest Bridge.
# Memory Usage: 14.4 MB, less than 69.81% of Python online submissions for Shortest Bridge.

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        n = len(A)
        self.n = n
        
        def isvalid(x,y):
            return 0 <= x < self.n and 0 <= y < self.n
        
        dirs = [[0, 1], [1, 0], [0,-1], [-1, 0]]
        
        # Find islands
        # Try to find boundary cells
        # Calculate minimum distance between any 2 cells from different islands
        
        # Find islands - BFS
        
        seen = {}
        edges_all = []
        
        for i in range(n):
            for j in range(n):
                
                if A[i][j] == 1 and seen.get((i, j)) == None:
                    edges = []
                    q = [[i, j]]
                    while q != []:
                        top = q.pop()
                        seen[(top[0], top[1])] = True       
                    
                        neig = 0

                        for d in dirs:
                            nxti = top[0] + d[0]
                            nxtj = top[1] + d[1]

                            if isvalid(nxti, nxtj):
                                if A[nxti][nxtj] == 1:
                                    neig += 1
                                    if seen.get((nxti, nxtj)) == None:
                                        q.append([nxti, nxtj])
                        
                        if neig < 4:
                            edges.append((top[0], top[1]))
                    
                    edges_all.append(edges)
        
        e1 = edges_all[0]
        e2 = edges_all[1]
        
        d2 = {}
        for i in e2:
            d2[i] = True
        
        # BFS from e1 to e2
        q = e1
        level = 0
        mem = {}
        while q != []:
            # print q
            next_level = []
            for top in q:
                mem[top] = True

                if top in d2:
                    return level - 1

                for dr in dirs:
                    nxti = top[0] + dr[0]
                    nxtj = top[1] + dr[1]

                    if isvalid(nxti, nxtj):
                        if mem.get((nxti, nxtj)) == None:
                            mem[(nxti, nxtj)] = True
                            next_level.append((nxti, nxtj))
            
            q = next_level
            level += 1