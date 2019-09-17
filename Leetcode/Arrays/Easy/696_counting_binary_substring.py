# Runtime: 132 ms, faster than 83.04% of Python online submissions for Count Binary Substrings.
# Memory Usage: 14.3 MB, less than 25.00% of Python online submissions for Count Binary Substrings.

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)
        prev = s[0]
        pcnt = 0
        ncnt = 1
        
        ans = 0
        
        for i in range(1, l):
            if s[i] != s[i-1]:
                ans += min(pcnt, ncnt)
                pcnt = ncnt
                ncnt = 1
            else:
                ncnt += 1
        
        ans += min(pcnt, ncnt)
        
        return ans