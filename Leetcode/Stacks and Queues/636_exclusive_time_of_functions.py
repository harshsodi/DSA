# Runtime: 68 ms, faster than 75.69% of Python online submissions for Exclusive Time of Functions.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Exclusive Time of Functions.

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        ans = [0 for _ in range(n)]
        
        st = []
        
        for log_ in logs:
            log = log_.split(":")
            pid = int(log[0])
            action = log[1]
            time = int(log[2])
            
            if st == []:
                st.append([pid, action, time])
            else:
                top = st[-1]
                
                if action == "start":
                    ans[top[0]] += time - top[2]
                    st.append([pid, action, time])
                else:
                    ans[pid] += 1 + time - top[2]
                    st.pop()
                    
                    if st != []:
                        st[-1][2] = time+1
        
        return ans