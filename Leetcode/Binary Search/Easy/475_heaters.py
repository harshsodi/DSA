# Runtime: 364 ms, faster than 26.57% of Python online submissions for Heaters.
# Memory Usage: 14.5 MB, less than 33.33% of Python online submissions for Heaters.

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        he = sorted(heaters)
        ho = houses
        
        ans = 0
        
        for i in ho:
            
            l = 0
            r = len(he) - 1
            
            while l < r:
                m = (l+r)/2
                
                if he[m] < i:
                    l = m+1
                else:
                    r = m
            
            # print i, he[max(0, l-1)], he[l]
            ans = max(ans, min(abs(i-he[l]), abs(i-he[max(0, l-1)])))
        
        return ans