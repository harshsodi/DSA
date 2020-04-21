# Runtime: 32 ms, faster than 62.89% of Python online submissions for String Matching in an Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for String Matching in

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        n = len(words)
        
        ans = set()
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                if words[i] in words[j]:
                    ans.add(words[i])
                    
        return ans