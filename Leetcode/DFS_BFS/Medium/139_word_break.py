# Runtime: 32 ms, faster than 40.80% of Python online submissions for Word Break.
# Memory Usage: 11.9 MB, less than 59.57% of Python online submissions for Word Break.

class Solution(object):
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # Use BFS
        
        n = len(wordDict)
        d = dict.fromkeys(wordDict, True)
        
        q = [s]
        v = {}
        
        while len(q):
            last = q.pop(0)
            
            tmp_word = ""
            for i in range(len(last)):
                tmp_word += last[i]
                
                if d.get(tmp_word) != None:    
                    rem = last[i+1:]
                    
                    if len(rem) == 0 or d.get(rem) != None:
                        return True
        
                    if v.get(rem) == None:
                        q.append(rem)
                        v[rem] = True
        
        return False