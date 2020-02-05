# Runtime: 1304 ms, faster than 25.19% of Python online submissions for Jump Game V.
# Memory Usage: 22.3 MB, less than 100.00% of Python online submissions for Jump Game V.

class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        
        n = len(arr)
        mem = {}
        
        def f(i):
            if mem.get(i):
                return mem[i]
            
            h = 0
            for j in range(1, d+1):
                nxt = i+j
                if nxt >= n or arr[nxt] >= arr[i]:
                    break
                
                h = max(h, f(nxt))
            
            for j in range(1, d+1):
                nxt = i-j
                if nxt < 0 or arr[nxt] >= arr[i]:
                    break
                
                h = max(h, f(nxt))
            
            mem[i] = h + 1
            return h + 1
        
        ans = 0
        for i in range(n):
            ans = max(ans, f(i))
            
        return ans