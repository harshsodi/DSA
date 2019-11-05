# Runtime: 28 ms, faster than 72.94% of Python online submissions for Remove K Digits.
# Memory Usage: 12.2 MB, less than 23.08% of Python online submissions for Remove K Digits.

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        # num = [int(x) for x in num]
        n = len(num)
        
        if n == 1 and k:
            return "0"
        
        st = []
        
        for i in range(0,n):
            if len(st) == 0:
                st.append(num[i])
            else:
                while k>0 and len(st) and st[-1] > num[i]:
                    st.pop()
                    k -= 1
                st.append(num[i])
        
        while k>0:
            k -= 1
            st.pop()
        
        i = 0
        while i < len(st) and st[i] == '0':
            i += 1
        
        ans = "".join(st[i:])
        if ans == "":
            return '0'
        return ans