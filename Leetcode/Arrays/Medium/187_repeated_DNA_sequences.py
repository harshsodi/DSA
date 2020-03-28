# Runtime: 56 ms, faster than 68.79% of Python online submissions for Repeated DNA Sequences.
# Memory Usage: 34 MB, less than 16.67% of Python online submissions for Repeated DNA Sequences.

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        n = len(s)
        ans = set()
        
        if n < 10:
            return []
        
        cst = s[:10]
        mem = {cst: True}
        
        for i in range(10, n):
            cst = cst[1:] + s[i]
            if mem.get(cst) != None:
                ans.add(cst)
            else:
                mem[cst] = True
        
        return ans