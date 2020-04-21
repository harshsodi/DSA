# Runtime: 20 ms, faster than 70.58% of Python online submissions for Last Stone Weight.
# Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Last Stone Weight.

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        n = len(stones)
        
        for i in range(n):
            # print stones
            if len(stones) == 0:
                return 0
            
            if len(stones) == 1:
                return stones[0]
            
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()