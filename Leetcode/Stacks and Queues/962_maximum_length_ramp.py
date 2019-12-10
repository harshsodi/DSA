# Runtime: 332 ms, faster than 68.07% of Python online submissions for Maximum Width Ramp.
# Memory Usage: 17.6 MB, less than 100.00% of Python online submissions for Maximum Width Ramp.

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        st = []
        
        ans = 0
        
        for i in range(n):
            if len(st) == 0:
                st.append(i)
            else:
                if A[st[-1]] <= A[i]:
                    ans = max(ans, i - st[-1])
                else:
                    st.append(i)
                
        print st
        print [A[x] for x in st]
        
        i = n-1
        lim = st[-1]
                
        while i > 0:
            while len(st) and A[st[-1]] <= A[i]:
                ans = max(ans, i - st[-1])
                st.pop()
                
            i -= 1
        
        return ans