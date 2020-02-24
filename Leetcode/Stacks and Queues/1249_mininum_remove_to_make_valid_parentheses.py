# Runtime: 1708 ms, faster than 12.94% of Python online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 22.3 MB, less than 100.00% of Python online submissions for Minimum Remove to Make Valid Parentheses.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        st = []
        d = {}
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                st.append(i)
                d[i] = True  
            if ch == ')':
                if len(st) and s[st[-1]] == '(':
                    x = st.pop()
                    d[x] = False
                else:
                    st.append(i)
                    d[i] = True
        
        ans = ""
        for i in range(len(s)):
            if not d.get(i):
                ans += s[i]
            
        return ans