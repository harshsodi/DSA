# Runtime: 376 ms, faster than 26.51% of Python online submissions for Push Dominoes.
# Memory Usage: 20.1 MB, less than 100.00% of Python online submissions for Push Dominoes.

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        n = len(dominoes)
        d = dominoes
        
        force = [0 for _ in range(n)]
        
        last_r = None
        for i in range(n):
            if d[i] == 'R':
                last_r = i
            
            if d[i] == 'L':
                last_r = None
            
            if last_r != None:
                force[i] += n - (i - last_r)
    
        last_l = None
        i = n-1
        while i >= 0:
            if d[i] == 'L':
                last_l = i
            
            if d[i] == 'R':
                last_l = None
            
            if last_l != None:
                force[i] -= n - (last_l - i)
            
            i -= 1
        
        ans = []
        for i in range(n):
            if d[i] == '.':
                if force[i] < 0:
                    ans.append('L')
                
                if force[i] > 0:
                    ans.append('R')
                
                if force[i] == 0:
                    ans.append('.')
            else:
                ans.append(d[i])
        
        return "".join(ans)