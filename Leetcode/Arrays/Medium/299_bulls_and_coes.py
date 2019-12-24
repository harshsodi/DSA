# Runtime: 32 ms, faster than 66.88% of Python online submissions for Bulls and Cows.
# Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Bulls and Cows.

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        
        bulls = 0
        cows = 0
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                secret = secret[:i] + 'a' + secret[i+1:]
                guess = guess[:i] + 'x' + guess[i+1:]
        
        sd = {}
        gd = {}
        
        for i in secret:
            sd[i] = sd.get(i, 0) + 1
        
        # print sd
        
        for g in guess:
            if sd.get(g):
                cows += 1
                sd[g] -= 1
        
        return str(bulls) + "A" + str(cows) + "B"