# Runtime: 252 ms, faster than 50.85% of Python online submissions for Hand of Straights.
# Memory Usage: 13.9 MB, less than 100.00% of Python online submissions for Hand of Straights.

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        n = len(hand)
        
        if n % W != 0:
            return False
        
        d = {}
        
        for i in hand:
            d[i] = d.get(i,0) + 1
        
        print d
        
        keys = sorted(d.keys())
        print keys
        
        for k in keys:
            v = d[k]
            
            if v > 0:
                for i in range(W):
                    if d.get(k+i) == None or d[k+i] < v:
                        return False
                    d[k+i] -= v
        
        return True