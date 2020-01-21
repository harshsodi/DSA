# Runtime: 8 ms, faster than 99.19% of Python online submissions for Detect Capital.
# Memory Usage: 11.7 MB, less than 66.67% of Python online submissions for Detect Capital.

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        n = len(word)
        valid = True
        
        allcap = True
        if word[-1] == word[-1].lower(): # Not capital
            allcap = False
        
        for i in range(0, n):
            if word[i] != word[i].lower(): # Capital
                if i > 0 and not allcap:
                    return False
            else:
                if allcap:
                    return False
        
        return True