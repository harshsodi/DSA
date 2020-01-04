# Runtime: 404 ms, faster than 11.60% of Python online submissions for Shortest Palindrome.
# Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Shortest Palindrome.

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        
        sr = s[::-1]
        
        
        ans = 0
        for i in (range(n)):
            # print i, n-i-1
            if s[:i+1] == sr[n-i-1:]:
                ans = i
        
        return sr[:n-ans-1] + s