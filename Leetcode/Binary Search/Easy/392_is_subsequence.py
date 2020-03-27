# Runtime: 300 ms, faster than 6.19% of Python online submissions for Is Subsequence.
# Memory Usage: 39.1 MB, less than 12.50% of Python online submissions for Is Subsequence.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def bs(arr, x):
            
            n = len(arr)
            l = 0
            r = n-1
            
            ans = -1
            
            while l <= r:
                m = (l+r)/2
                
                if arr[m] > x:
                    ans = arr[m]
                    r = m-1
                else:
                    l = m+1
            
            return ans
    
        # Make map
        d = [[] for _ in range(26)]
        
        for i_ in range(len(t)):
            i = t[i_]
            d[ord(i) - ord('a')].append(i_)
            
        last_ch = -1
        for i in s:
            ch = ord(i)-ord('a')
            nxt = bs(d[ch], last_ch)
            
            if nxt == -1:
                return False
            else:
                last_ch = nxt
        
        return True