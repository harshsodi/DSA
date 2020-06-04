# Runtime: 48 ms, faster than 61.45% of Python online submissions for Find Common Characters.
# Memory Usage: 12.9 MB, less than 5.88% of Python online submissions for Find Common Characters.

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        ans = [0 for _ in range(26)]
        acode = ord('a')
        
        seed = A[0]
        for i in seed:
            ind = ord(i) - acode
            # print ind
            ans[ind] += 1
    
        for word in A[1:]:
            local = [0 for _ in range(26)]
            for j in word:
                lind = ord(j) - acode
                local[lind] += 1
            
            for i in range(26):
                ans[i] = min(ans[i], local[i])
        
        # print ans
        
        ret = []
        for i in range(26):
            ch = chr(i + acode)
            ret += [ch] * ans[i]
            
        return ret