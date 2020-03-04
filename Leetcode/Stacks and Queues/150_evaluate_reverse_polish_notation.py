# Runtime: 64 ms, faster than 29.59% of Python online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 13.7 MB, less than 28.57% of Python online submissions for Evaluate Reverse Polish Notation.

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import math
        n = len(tokens)
        if n == 0:
            return 0
        
        st = []
        
        for i in tokens:
                        
            if i == '+':
                st.append(st.pop() + st.pop())
                
            if i == '-':
                o1 = st.pop()
                o2 = st.pop()
                st.append(o2 - o1)
            
            if i == '*':
                st.append(st.pop() * st.pop())
            
            if i == '/':
                o1 = st.pop()
                o2 = st.pop()
                
                if o1*o2 < 0:
                    st.append(int(math.ceil(o2*1.0/o1)))
                else:
                    st.append(o2/o1)
            
            if i not in ['+', '-', '*', '/']:
                st.append(int(i))
        
        return st[0]