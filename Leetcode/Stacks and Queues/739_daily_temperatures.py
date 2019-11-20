# Runtime: 444 ms, faster than 66.36% of Python online submissions for Daily Temperatures.
# Memory Usage: 15.1 MB, less than 53.85% of Python online submissions for Daily Temperatures.

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        n = len(T)
        ans = [0 for _ in T]
        
        st = []
        for i in range(n):
            while st != [] and T[st[-1]] < T[i]:
                ind = st.pop()
                ans[ind] = i - ind
            st.append(i)
        
        return ans