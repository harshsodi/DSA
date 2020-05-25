# Runtime: 128 ms, faster than 63.82% of Python online submissions for Find All Anagrams in a String.
# Memory Usage: 13.4 MB, less than 5.88% of Python online submissions for Find All Anagrams in a String.

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        n = len(s)
        m = len(p)
        
        req = {}
        for i in p:
            req[i] = req.get(i, 0) + 1
        
        uniq = len(req.keys())
        # print uniq
        
        l = 0
        r = 0
        
        good = 0
        d = {}
        ans = []
        
        while r < n:
            
            """
            r -> starting from l fo till l + len(p)
            if unwanted element found in between, jump the window r = r+1 and l=r
            else while expanding keep frequency and count of good chars
                as soon as good char hits uniq(p) we have an answer
                slide window by 1 until unwanted char found on r
            """
            
            if l > n - m:
                break
            
            conc = True
            for i in range(m):
                r = l+i
                if req.get(s[r]) == None:
                    l = r+1
                    conc = False
                    break
                else:
                    d[s[r]] = d.get(s[r], 0) + 1
                    if d[s[r]] == req[s[r]]:
                        good += 1
                        if uniq == good:
                            ans.append(l)
                                 
            if not conc:
                continue
            
            conc = True
            while r < n:
                
                d[s[l]] -= 1
                if d[s[l]] < req[s[l]]:
                    good -= 1
                l += 1
                r += 1
                
                
                if r == n:
                    break
                    
                if req.get(s[r]) == None:
                    l = r+1
                    conc = False
                    break
                else:
                    d[s[r]] = d.get(s[r], 0) + 1
                    if req[s[r]] == d[s[r]]:
                        good += 1
                    if good == uniq:
                        ans.append(l)
        
        return ans