# Runtime: 56 ms, faster than 62.73% of Python online submissions for DI String Match.
# Memory Usage: 13.3 MB, less than 9.52% of Python online submissions for DI String Match.

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        l = len(S)        
        a = [i for i in range(l+1)]
        
        L = 0
        H = l
        
        for i in range(l):
            if S[i] == 'D':
                a[i] = H
                H -= 1
            else:
                a[i] = L
                L += 1
        
        if S[i] == 'D':
            a[i+1] = L
        else:
            a[i+1] = H
        
        return a