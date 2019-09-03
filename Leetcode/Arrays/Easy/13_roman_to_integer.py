# Runtime: 36 ms, faster than 78.69% of Python online submissions for Roman to Integer.
# Memory Usage: 11.7 MB, less than 79.03% of Python online submissions for Roman to Integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        print s
        
        ans = 0
        
        prev = d[s[0]]
        curr = 0
        
        for i in range(1, len(s)):
            curr = d[s[i]]
            # print prev, curr
            if prev >= curr:
                ans += prev
            else:
                ans -= prev
            prev = curr
            
        ans += d[s[len(s)-1]]
        
        return ans