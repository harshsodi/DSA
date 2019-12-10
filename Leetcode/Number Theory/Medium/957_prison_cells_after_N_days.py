# Runtime: 20 ms, faster than 92.33% of Python online submissions for Prison Cells After N Days.
# Memory Usage: 11.8 MB, less than 28.57% of Python online submissions for Prison Cells After N Days.

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        # Find pattern
        d = {}
        j = 0
        
        prev = [_ for _ in cells]
        rep = -1
        f = False
        
        n = N
        
        while N:
            
            nxt = [0,0,0,0,0,0,0,0]
            for i in range(1,7):
                if prev[i-1] == prev[i+1]:
                    nxt[i] = 1
                
            prev = nxt
        
            t = tuple(nxt)

            if d.get(t):
                rep = j - d[t]
                f = True
                break
            else:
                d[t] = j
        
            j += 1
            N -= 1
        
        x = n
        if rep >= 0:
            x = (n-1)%rep + 1
        else:
            return prev
        
        prev = [_ for _ in cells]
        
        for j in range(x):
            
            nxt = [0,0,0,0,0,0,0,0]
            for i in range(1,7):
                if prev[i-1] == prev[i+1]:
                    nxt[i] = 1
                
            prev = nxt
            
        return prev