# Runtime: 1744 ms, faster than 18.18% of Python online submissions for Number of Matching Subsequences.
# Memory Usage: 16.7 MB, less than 33.33% of Python online submissions for Number of Matching Subsequences.

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
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
    
        d = [[] for i in range(26)]
        for i in range(len(S)):
            d[ord(S[i]) - ord('a')].append(i)
        
        ans = 0
        
        for word in words:
            last_ch = -1
            
            fnd = 1
            for i in word:
                ind = bs(d[ord(i) - ord('a')], last_ch)
                
                if ind == -1:
                    fnd = 0
                    break
                else:
                    last_ch = ind
            
            ans += fnd
        
        return ans