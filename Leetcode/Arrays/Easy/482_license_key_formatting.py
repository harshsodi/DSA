# Runtime: 484 ms, faster than 40.14% of Python online submissions for License Key Formatting.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for License Key Formatting.

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        n = len(S)
        
        i = n-1
        ans = ""
        cnt = 0
        
        while i >= 0:
            
            if S[i] == '-':
                i -= 1
                continue
            
            if cnt == K:
                ans = '-' + ans
                cnt = 0
            
            ans = S[i].upper() + ans
            cnt += 1
            
            i -= 1
        
        return ans