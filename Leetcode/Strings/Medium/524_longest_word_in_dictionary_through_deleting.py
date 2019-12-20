# Runtime: 372 ms, faster than 54.33% of Python online submissions for Longest Word in Dictionary through Deleting.
# Memory Usage: 16.7 MB, less than 100.00% of Python online submissions for Longest Word in Dictionary through Deleting.

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        n = len(s)
        
        ans = None
        
        for word in d:
            
            m = len(word)
            
            if m > n:
                continue
            
            i = 0
            
            for c in word:
                # print "Looking for ", c
                while i<n:
                    if s[i] == c:
                        break
                    else:
                        i += 1
                # print "Found at ", i
                i += 1
                    
            if i <= n:
                if ans == None:
                    ans = word
                elif len(ans) < len(word):
                    ans = word
                elif len(ans) == len(word):
                    ans = min(ans, word)
        
        if ans == None:
            return ""
        return ans