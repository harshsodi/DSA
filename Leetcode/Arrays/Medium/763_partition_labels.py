# Runtime: 28 ms, faster than 61.74% of Python online submissions for Partition Labels.
# Memory Usage: 11.8 MB, less than 17.65% of Python online submissions for Partition Labels.

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        n = len(S)
        l = []
        d = {}
        
        for i in range(n):
            if d.get(S[i]) == None:
                d[S[i]] = len(l)
                l.append([i,None])
        
        for i in reversed(range(n)):
            if d.get(S[i]) != None:
                l[d[S[i]]][1] = i
                d[S[i]] = None
        
        s = l[0][0]
        e = l[0][1]
        
        ans = []
        
        for i in range(1, len(l)):
            e_t = l[i][1]
            s_t = l[i][0]
            
            if s_t < e:
                e = max(e, e_t)
            else:
                ans.append(e-s+1)
                s = s_t
                e = e_t
        
        ans.append(e-s+1)
        
        return ans