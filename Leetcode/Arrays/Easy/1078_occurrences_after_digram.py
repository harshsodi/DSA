# Runtime: 16 ms, faster than 70.05% of Python online submissions for Occurrences After Bigram.
# Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Occurrences After Bigram.

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        ans = []
        
        words = text.split()
        n = len(words)
        if n < 3:
            return []
        
        for i in range(n-2):
            if words[i] == first and words[i+1] == second:
                ans.append(words[i+2])
        
        return ans