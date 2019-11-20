# Runtime: 120 ms, faster than 73.02% of Python online submissions for Is Subsequence.
# Memory Usage: 19 MB, less than 75.00% of Python online submissions for Is Subsequence.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        st = []
        for i in s:
            st.append(i)
        
        # print st
        
        for i in t:
            if len(st) and st[0] == i:
                st.pop(0)
        
        if len(st):
            return False
        return True