# Runtime: 240 ms, faster than 21.42% of Python online submissions for Longest Repeating Character Replacement.
# Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Longest Repeating Character Replacement.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        n = len(s)

        if n <= 1:
            return n
        
        def c2i(c):
            return ord(c) - ord('A')
        
        h = dict.fromkeys(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 0)
        
        l = 0
        r = 0
        
        tot = 0
        mx = 0
        ans = 1

        h[s[0]] = 1
        
        while l < n-1:
            while r < n-1:
                r += 1
                
                h[s[r]] += 1
                if mx < h[s[r]]:
                    mx = h[s[r]]
                
                if k < (r-l+1) - mx:
                    break
                else:
                    ans = max(ans, r-l+1)
            
            while l<r:
                h[s[l]] -= 1
                mx = max(h.values())
                
                l += 1
                
                if k >= (r-l+1) - mx:
                    break
                else:
                    ans = max(ans, r-l+1)
                    
        return ans