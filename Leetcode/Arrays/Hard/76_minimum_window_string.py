# Runtime: 108 ms, faster than 65.18% of Python online submissions for Minimum Window Substring.
# Memory Usage: 13.7 MB, less than 46.43% of Python online submissions for Minimum Window Substring.

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        n = len(s)
        m = len(t)
        
        if m > n:
            return ""
        
        reqd = {}
        for i in t:
            reqd[i] = reqd.get(i, 0) + 1
    
        req = len(reqd.keys())
        fnd = 0
        
        curd = {}
        
        l = 0
        r = 0
        
        maxl = float('inf')
        ans = [-1, -1]
        
        while r < n:
            
            # print r
            
            while r < n and fnd < req:
                
                if reqd.get(s[r]) == None:
                    r += 1
                    continue
                
                curd[s[r]] = curd.get(s[r], 0) + 1
                
                if reqd[s[r]] == curd[s[r]]:
                    fnd += 1
                
                r += 1
        
            while l < r and fnd >= req:
                
                ln = r - l
                if ln < maxl:
                    maxl = ln
                    ans = [l, r]
                
                if reqd.get(s[l]) == None:
                    l += 1
                    continue
                
                curd[s[l]] -= 1
                
                if reqd[s[l]] > curd[s[l]]:
                    fnd -= 1
                
                l += 1
        
        if ans[0] == -1:
            return ""
        else:
            return s[ans[0]: ans[1]]