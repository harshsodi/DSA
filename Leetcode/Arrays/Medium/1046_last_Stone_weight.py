# Runtime: 32 ms, faster than 10.86% of Python online submissions for Last Stone Weight.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Last Stone Weight.

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        # By bucket sort
        
        n = 1000
        buckets = [0 for _ in range(n+1)]
        
        for i in stones:
            buckets[i] += 1
        
        i = n
        while i > 0:
            if buckets[i] > 0:
                
                buckets[i] %= 2
                if buckets[i] == 0:
                    continue
                
                j = i-1
                while j > 0 and buckets[j] == 0:                    
                    j -= 1
                        
                if j == 0:
                    return i
            
                buckets[i-j] += 1
                buckets[j] -= 1
                
            i -= 1
        
        return 0