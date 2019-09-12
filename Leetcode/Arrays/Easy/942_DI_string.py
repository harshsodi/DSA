# Runtime: 64 ms, faster than 25.76% of Python online submissions for DI String Match.
# Memory Usage: 13.4 MB, less than 9.52% of Python online submissions for DI String Match.

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        l = len(S)
        
        a = [i for i in range(l+1)]
        
        for i in range(l):
            if S[i] == 'D':
                j = i
                while j > -1:
                    if S[j] == 'D':
                        temp = a[j+1]
                        a[j+1] = a[j]
                        a[j] = temp
                    else:
                        break
                    
                    j -= 1
                    
        return a