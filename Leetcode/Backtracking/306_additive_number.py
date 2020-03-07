# Runtime: 8 ms, faster than 98.67% of Python online submissions for Additive Number.
# Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Additive Number.

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        n = len(num)
        
        def isvalid(ni):
            return not (len(ni) > 1 and ni[0] == '0')
                
        def f(n1, n2, n3):
            
            if not (isvalid(n1) and isvalid(n2)):
                return False
            
            sm = str(int(n1) + int(n2))
            
            if n3 == sm:
                return True
            
            if n3.startswith(sm):
                return f(n2, sm, n3[len(sm):])
        
            return False
        
        for i in range(1, n):
            for j in range(1, n):
                
                if f(num[:i], num[i:i+j], num[i+j:]):
                    return True