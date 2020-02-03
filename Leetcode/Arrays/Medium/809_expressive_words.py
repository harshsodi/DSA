# Runtime: 36 ms, faster than 86.30% of Python online submissions for Expressive Words.
# Memory Usage: 12 MB, less than 25.00% of Python online submissions for Expressive Words.

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        
        n = len(words)
        m = len(S)
        
        master = []
        
        curr = S[0]
        cnt = 0
        for i in range(m):
            if S[i] != curr:
                master.append([curr, cnt])
                curr = S[i]
                cnt = 1
            else:
                cnt += 1
        
        master.append([curr, cnt])
        
        ans = 0
        
        for word in words:
            
            wordmap = []
            
            curr = word[0]
            cnt = 0
            for i in range(len(word)):
                if word[i] != curr:
                    wordmap.append([curr, cnt])
                    curr = word[i]
                    cnt = 1
                else:
                    cnt += 1
            
            wordmap.append([curr, cnt])
            
            valid = True
            if len(wordmap) != len(master):
                valid = False
            else:
                for i in range(len(wordmap)):
                    wm = wordmap[i]
                    ms = master[i]
                    
                    if wm[0] != ms[0]:
                        valid = False
                        break
                    else:
                        if wm[1] > ms[1]:
                            valid = False
                            break
                        elif wm[1] != ms[1] and ms[1] < 3:
                            valid = False
                            break
            
            if valid:
                ans += 1
            
        return ans