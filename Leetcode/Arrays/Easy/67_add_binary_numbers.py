# Runtime: 32 ms, faster than 14.87% of Python online submissions for Add Binary.
# Memory Usage: 11.8 MB, less than 23.68% of Python online submissions for Add Binary.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        sa = []
        sb = []
        
        for i in a:
            sa.append(int(i))
        for i in b:
            sb.append(int(i))
        
        ans = []
        
        c = 0
        
        while sa and sb:
            x = sa.pop()
            y = sb.pop()
        
            tmp = x+y+c
            if tmp > 1:
                c = 1
                tmp = tmp%2
            else:
                c = 0
            ans = [tmp] + ans
        
        print ans
        
        while sa:
            tmp = sa.pop()+c
            if tmp > 1:
                c = 1
                tmp = tmp%2
            else:
                c = 0
            ans = [tmp] + ans
            
        while sb:
            tmp = sb.pop()+c
            
            if tmp > 1:
                c = 1
                tmp = tmp%2
            else:
                c = 0
                
            ans = [tmp] + ans
            
        if c:
            ans = [1] + ans
        
        return "".join(map(str, ans))