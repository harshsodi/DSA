# Runtime: 208 ms, faster than 64.23% of Python online submissions for Jump Game III.
# Memory Usage: 17.1 MB, less than 100.00% of Python online submissions for Jump Game III.

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        n = len(arr)
        
        q = [start]
        v = {}
        while len(q):
            top = q.pop(0)
            
            l = top - arr[top]
            r = top + arr[top]
            
            if l >= 0 and not v.get(l):
                if arr[l] == 0:
                    return True
                q.append(l)
                v[l] = True
            
            if r < n and not v.get(r):
                if arr[r] == 0:
                    return True
                q.append(r)
                v[r] = True
        
        return False