# Runtime: 76 ms, faster than 31.77% of Python online submissions for Reconstruct Itinerary.
# Memory Usage: 12.5 MB, less than 38.46% of Python online submissions for Reconstruct Itinerary.

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        g = {}
        v = {}
        
        for i in tickets:
            frm = i[0]
            to = i[1]
            
            if g.get(frm) == None:
                g[frm] = [to]
            else:
                g[frm].append(to)
            
        for i in g:
            g[i] = sorted(g[i])
        
        def f(g, ans, curr, reqlen):

            # print ans
    
            if len(ans) == reqlen:
                return ans
            
            x = g.get(curr, [])
            
            for i in range(len(x)):
                
                p = g[curr]
                g[curr] = g[curr][:i] + g[curr][i+1:]
                
                a = f(g, ans + [x[i]], x[i], reqlen)
                if a:
                    return a
                
                g[curr] = p
        
        return f(g, ["JFK"], "JFK", len(tickets) + 1)