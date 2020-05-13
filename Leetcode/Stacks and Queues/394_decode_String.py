# Runtime: 12 ms, faster than 93.76% of Python online submissions for Decode String.
# Memory Usage: 12.7 MB, less than 5.88% of Python online submissions for Decode String.

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        2[abc3[cd]ef]
        """
        
        n = len(s)
        numalpha = "0123456789"
        
        st = [[1, ""]]
        i = 0
        while i < n:
            # print i, st
            if s[i] in numalpha:
                nums = ""
                while s[i] in numalpha:
                    nums += s[i]
                    i += 1
                    
                num = int(nums)
                st.append([num, ""])
            elif s[i] == ']':
                cstr = st[-1][1] * st[-1][0]
                st.pop()
                st[-1][1] += cstr
            else:
                st[-1][1] += s[i]
                
            i += 1
        
        return st[0][1]