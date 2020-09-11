# Runtime: 516 ms, faster than 51.32% of Python online submissions for Substring with Concatenation of All Words.
# Memory Usage: 13.5 MB, less than 38.13% of Python online submissions for Substring with Concatenation of All Words.

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        n = len(s)
        m = len(words[0])
        ws = len(words)
        
        d = {}
        for i in words:
            if d.get(i) != None:
                d[i][0] += 1
                d[i][1] += 1
            else:
                d[i] = [1,1]
        
        ans = []
        
        for i in range(n - (m)*ws + 1):
            
            j, cnt = i, 0
            succ = True
            
            for cnt in range(ws):
                wrd = s[j: j+m]
                
                if d.get(wrd) == None:
                    succ = False
                    break
                else:
                    if d[wrd][1] <= 0:
                        succ = False
                        break
                    else:
                        d[wrd][1] -= 1
                
                j += m
            
            if succ:
                ans.append(i) 
            
            
            # Reset routine
            for x in d:
                d[x][1] = d[x][0]
        
        return ans