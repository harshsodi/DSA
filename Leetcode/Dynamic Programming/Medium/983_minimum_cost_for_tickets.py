# Runtime: 16 ms, faster than 99.68% of Python online submissions for Minimum Cost For Tickets.
# Memory Usage: 11.7 MB, less than 58.33% of Python online submissions for Minimum Cost For Tickets.

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        d = dict.fromkeys(days, True)
        
        dp = [0 for i in range(366)]
        
        for i in range(1, 366):
            
            if d.get(i) == None:
                dp[i] = dp[i-1]
            else:
                day = max(0, i-1)
                week = max(0, i-7)
                month = max(0, i-30)

                dp[i] = min([dp[day] + costs[0], dp[week] + costs[1], dp[month] + costs[2]])
        
        return dp[365]