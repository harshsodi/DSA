# Runtime: 28 ms, faster than 56.27% of Python online submissions for Two City Scheduling.
# Memory Usage: 11.8 MB, less than 31.82% of Python online submissions for Two City Scheduling

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        n = len(costs)
        
        t = []
        for i in costs:
            t.append(i + [i[0] - i[1]]) # How much it is costlier to send him to A
        
        t = sorted(t, key=lambda x: x[2])
        
        ans = 0
        
        for i in range(n/2):
            ans += t[i][0] + t[i+n/2][1]
        
        return ans