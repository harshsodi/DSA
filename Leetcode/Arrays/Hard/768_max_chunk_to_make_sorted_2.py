# Runtime: 60 ms, faster than 91.49% of Python online submissions for Max Chunks To Make Sorted II.
# Memory Usage: 12 MB, less than 33.33% of Python online submissions for Max Chunks To Make Sorted II.

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        ans = 0
        
        sarr = sorted(arr)
        
        dsor = {}
        dact = {}
        
        diff = 0
        
        for i in range(n):
            sor = sarr[i]
            act = arr[i]
            
            if dact.get(sor):
                dact[sor] -= 1
                diff -= 1
            else:
                dsor[sor] = dsor.get(sor, 0) + 1
                diff += 1
                
            if dsor.get(act):
                dsor[act] -= 1
                diff -= 1
            else:
                dact[act] = dact.get(act, 0) + 1
                diff += 1
            
            if diff == 0:
                ans += 1
            
        return ans