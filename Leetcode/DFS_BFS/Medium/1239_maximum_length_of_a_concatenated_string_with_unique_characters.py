# Runtime: 352 ms, faster than 27.97% of Python online submissions for Heaters.
# Memory Usage: 14.4 MB, less than 66.67% of Python online submissions for Heaters.

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        # convert to bitmap
        def bm(string):
            ans = 0
            
            for ch in string:
                x = ord(ch) - ord('a')
                tmp = ans | pow(2, x)
                
                if tmp == ans:
                    return None
                ans = tmp
            
            return ans
        
        a = []
        b = []
    
        ans = 0
    
        for s in arr:
            x = bm(s)
            a.append(x)
            if x != None:
                b.append(True)
                ans =  max(ans, len(s))
            else:
                b.append(False)
        
        n = len(a)
        
        q = []
        for i in range(n):
            if b[i]:
                q.append(([i], a[i], len(arr[i])))
        
        while len(q):
            # print q
            top = q.pop(0)
            
            last = top[0][-1]
            ln = top[2]
            mask = top[1]
            
            for i in range(last+1, n):
                
                if not b[i]:
                    continue
                
                res = a[i] & mask
                if res == 0:
                    ans = max(ans, len(arr[i]) + ln)
                    q.append((top[0]+[i], a[i] | mask, ln+len(arr[i])))
        
        return ans