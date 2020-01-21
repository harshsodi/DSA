# Runtime: 112 ms, faster than 92.08% of Python online submissions for Maximize Distance to Closest Person.
# Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Maximize Distance to Closest Person.

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        n = len(seats)
        
        last_seat = -1
        ans = 0
        
        for i in range(n):
            if seats[i] == 1:
                if last_seat == -1:
                    ans = i
                ans = max(ans, (i - last_seat) - (i - last_seat + 1)/2)
                last_seat = i
            
        ans = max(ans, n-last_seat-1)
        
        return ans