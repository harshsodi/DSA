# Runtime: 11608 ms, faster than 34.09% of Python online submissions for Similar String Groups.
# Memory Usage: 17.2 MB, less than 100.00% of Python online submissions for Similar String Groups.

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        A = list(set(A))
        
        def issim(str1, str2):
            if str1 == str2:
                return True
            
            m = len(str1)
            
            diff = 0
            for i in range(m):
                if str1[i] != str2[i]: 
                    diff += 1
                
                if diff > 2:
                    return False
            
            return True
        
        n = len(A)
        g = {}
        
        def dfs(root):
            if seen.get(root) != None:
                return
            seen[root] = True
            
            for ch in g.get(root,[]):
                if seen.get(ch) == None:
                    dfs(ch)
        
        # Create graph
        for i in range(n):
            for j in range(i+1, n):
                if issim(A[i], A[j]):
                    
                    if g.get(A[i]) == None:
                        g[A[i]] = [A[j]]
                    else:
                        g[A[i]].append(A[j])
                    
                    if g.get(A[j]) == None:
                        g[A[j]] = [A[i]]
                    else:
                        g[A[j]].append(A[i])
                    
        # Find number of CC's
        cc = 0
        seen = {}
        
        for i in A:
            if seen.get(i) != None:
                continue
            else:
                cc += 1
                dfs(i)
        
        return cc