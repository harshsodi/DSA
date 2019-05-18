# Runtime: 52 ms, faster than 97.14% of Python online submissions for Palindrome Number.
# Memory Usage: 11.7 MB, less than 76.43% of Python online submissions for Palindrome Number.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return str(x) == "".join(reversed(str(x)))