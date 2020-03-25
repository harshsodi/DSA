# Runtime: 24 ms, faster than 53.27% of Python online submissions for Unique Morse Code Words.
# Memory Usage: 11.8 MB, less than 28.57% of Python online submissions for Unique Morse Code Words.

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        n = len(words)
        
        alp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d = {}
        
        for i in range(n):
            word = words[i]
            code = ""
            
            for ch in word:
                code += alp[ord(ch) - ord('a')]
            
            d[code] = True
        
        return len(d.keys()) 