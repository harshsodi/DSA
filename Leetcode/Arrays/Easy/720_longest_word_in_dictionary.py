# Runtime: 160 ms, faster than 16.67% of Python online submissions for Longest Word in Dictionary.
# Memory Usage: 12.4 MB, less than 75.00% of Python online submissions for Longest Word in Dictionary.

class Solution(object):
def longestWord(self, words):
    """
    :type words: List[str]
    :rtype: str
    """
    
    d = dict.fromkeys(words, True)
    ans = None
    
    for word in words:
        tmp = ""
        
        ans_found = True
        for char in word:
            tmp += char
            # print tmp
            if d.get(tmp) == None:
                ans_found = False
                break
        
        if ans_found:
            if not ans:
                ans = word
            else:
                if len(ans) < len(word):
                    ans = word
                elif len(ans) == len(word):
                    ans = min(ans, word)
            
    return ans