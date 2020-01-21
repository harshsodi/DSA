# Runtime: 840 ms, faster than 20.56% of Python online submissions for Corporate Flight Bookings.
# Memory Usage: 25.5 MB, less than 100.00% of Python online submissions for Corporate Flight Bookings.

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        ans = [0 for _ in range(n)]
        s = [0 for _ in range(n)]
        e = [0 for _ in range(n)]
        
        for b in bookings:
            st = b[0]
            en = b[1]
            qn = b[2]
            
            s[st - 1] += qn
            e[en - 1] += qn
            
        ans[0] = s[0]
        for i in range(1, n):
            ans[i] = ans[i-1] + s[i] - e[i-1]
        
        return ans