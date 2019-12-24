# Runtime: 60 ms, faster than 85.92% of Python online submissions for Get Equal Substrings Within Budget.
# Memory Usage: 16.8 MB, less than 100.00% of Python online submissions for Get Equal Substrings Within Budget.

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        
        n = len(s)
        
        if n == 0:
            return 0
        
        diff = [abs(ord(s[x]) - ord(t[x])) for x in range(len(s))]
        
        l = 0
        r = 0
        
        total = 0        
        ln = 0
        maxl = 0
        
        while r < n:
            total += diff[r]
            r += 1
            ln += 1
            if total <= maxCost:
                maxl = max(maxl, ln)
            else:
                while l<r and total > maxCost:
                    total -= diff[l]
                    l += 1
                    ln -= 1
                maxl = max(maxl, ln)
        
        return maxl