# Runtime: 20 ms, faster than 81.16% of Python online submissions for Longest Palindrome.
# Memory Usage: 11.8 MB, less than 12.50% of Python online submissions for Longest Palindrome.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        pairs = 0
        singles = 0
        
        d = {}
        
        for i in s:
            if not d.get(i):
                singles += 1
                d[i] = True
            else:
                pairs += 1
                singles -= 1
                d[i] = False
        
        ans = pairs * 2
        if singles:
            return ans + 1
        return ans