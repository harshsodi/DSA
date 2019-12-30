# Runtime: 144 ms, faster than 51.52% of Python online submissions for Valid Palindrome II.
# Memory Usage: 12.7 MB, less than 55.56% of Python online submissions for Valid Palindrome II.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n = len(s)
        
        def f(st, i, j, sinned):
            while i < j:
                if st[i] != st[j]:
                    
                    if sinned:
                        return False
                    
                    return f(st, i+1, j, True) or f(st, i, j-1, True)
                    break
                
                i += 1
                j -= 1
            
            return True
    
        return f(s, 0, n-1, False)