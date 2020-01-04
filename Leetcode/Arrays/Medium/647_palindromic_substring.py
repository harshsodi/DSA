# Runtime: 92 ms, faster than 87.34% of Python online submissions for Palindromic Substrings.
# Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Palindromic Substrings.

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        ans = 0
        
        centers = []
        
        for i in range(n):
            ans += 1
            centers.append((i,i))
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                centers.append((i, i+1))
                ans += 1
    
        for c in centers:
            l = c[0] - 1
            r = c[1] + 1
            
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    ans += 1
                else:
                    break
                
                l -= 1
                r += 1
        
        return ans