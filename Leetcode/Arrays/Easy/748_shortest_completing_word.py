# Runtime: 116 ms, faster than 41.84% of Python online submissions for Shortest Completing Word.
# Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Shortest Completing Word.

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        n = len(words)
        
        ans = None
        
        start = 0
        end = ord('z') - ord('a')
        
        def f(ch):
            return ord(ch) - ord('a')
        
        mem = [0 for _ in range(26)]
        
        for i in licensePlate.lower():
            x = f(i)
            
            if x >=0 and x <= 25:
                mem[x] += 1
        
        for word in words:
            tmem = [0 for _ in range(26)]
            
            for i in word:
                x = f(i)
                tmem[x] += 1
            
            val = True
            
            for i in range(26):
                if mem[i] > tmem[i]:
                    val = False
                    break
            
            if val:
                if ans == None:
                    ans = word
                else:
                    if len(ans) > len(word):
                        ans = word
                        
        return ans