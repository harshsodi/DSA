# Runtime: 384 ms, faster than 94.20% of Python online submissions for Divide Array in Sets of K Consecutive Numbers.
# Memory Usage: 27.6 MB, less than 100.00% of Python online submissions for Divide Array in Sets of K Consecutive Numbers.

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        keys = sorted(d.keys())
        
        for key in keys:
            cnt = d[key]
            
            if cnt > 0:
                for i in range(key, key+k):
                    
                    if d.get(i) == None or d[i] < cnt:
                        return False
                    d[i] -= cnt
                    
        return True