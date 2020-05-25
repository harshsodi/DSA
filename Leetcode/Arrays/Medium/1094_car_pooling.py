# Runtime: 80 ms, faster than 22.33% of Python online submissions for Car Pooling.
# Memory Usage: 13.1 MB, less than 100.00% of Python online submissions for Car Pooling.

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        inc = {}
        dec = {}
        mx = 0
        
        st = float('inf')
        en = float('-inf')
        
        for i in trips:
            inc[i[1]] = inc.get(i[1], 0) + i[0]
            dec[i[2]] = dec.get(i[2], 0) + i[0]
        
            st = min(st, i[1])
            en = max(en, i[2])
        
        cnt = 0
        for i in range(st, en + 1):
            cnt += inc.get(i, 0)
            cnt -= dec.get(i, 0)
            
            mx = max(cnt, mx)
        
        if mx <= capacity:
            return True
    
        return False