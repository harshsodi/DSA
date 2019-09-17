# Runtime: 148 ms, faster than 56.23% of Python online submissions for Can Place Flowers.
# Memory Usage: 12.1 MB, less than 20.00% of Python online submissions for Can Place Flowers.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return True
        
        l = len(flowerbed)
        
        prev = 0
        cnt = 0
        
        for i in range(l):
            
            if i == l-1:
                nxt = 0
            else:
                nxt = flowerbed[i+1]
                
            if flowerbed[i] == 0:
                if prev == 0 and nxt == 0:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt == n:
                        return True
            
            prev = flowerbed[i]
            
        return False