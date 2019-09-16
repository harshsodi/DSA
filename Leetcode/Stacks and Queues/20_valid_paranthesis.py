# Runtime: 8 ms, faster than 99.50% of Python online submissions for Valid Parentheses.
# Memory Usage: 11.8 MB, less than 56.30% of Python online submissions for Valid Parentheses.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        d = {')':'(', ']':'[', '}':'{'}
        k = d.keys()
        
        st = []
        
        for i in s:
            if st == []:
                if i in k:
                    return False
                t = None
            else:
                t = st[-1]
            
            if d.get(i):    
                if t != d[i]:
                    return False
                st.pop()
            else:
                st.append(i)
        
        if st == []:
            return True
        return False