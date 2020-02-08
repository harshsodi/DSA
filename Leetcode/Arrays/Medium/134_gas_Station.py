# Runtime: 40 ms, faster than 62.22% of Python online submissions for Gas Station.
# Memory Usage: 12.6 MB, less than 36.36% of Python online submissions for Gas Station.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(gas)
        
        total = 0
        s = 0
        indx = 0
        
        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            s += diff
            if s < 0:
                s = 0
                indx = i + 1
        
        if total < 0:
            return -1
        
        return indx