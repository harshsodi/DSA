# Runtime: 56 ms, faster than 31.23% of Python online submissions for Valid Palindrome.
# Memory Usage: 12.5 MB, less than 84.31% of Python online submissions for Valid Palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n = len(s)
        d = {}
        
        alpha = {}
        for i in "abcdefghijklmnopqrstuvwxyz0123456789":
            alpha[i] = True
        
        l = 0
        r = n-1
        
        while l < r:
            while alpha.get(s[l].lower()) == None and l < n-1:
                l += 1
            
            while alpha.get(s[r].lower()) == None and r > 0:
                r -= 1
            
            if l >= r:
                return True
            
            if s[l].lower() != s[r].lower():
                return False
    
            l += 1
            r -= 1
    
        return True