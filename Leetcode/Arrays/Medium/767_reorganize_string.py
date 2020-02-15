# Runtime: 20 ms, faster than 79.20% of Python online submissions for Reorganize String.
# Memory Usage: 11.8 MB, less than 20.00% of Python online submissions for Reorganize String.

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        n = len(S)
        
        d = {}
        for i in S:
            d[i] = d.get(i,0) + 1
        
        print d
        mp = list(sorted([(k, d[k]) for k in d.keys()], key=lambda x:x[1], reverse=True))
        
        print mp
        
        ques = ""
        
        for ch in mp:
            times = ch[1]
            ques += ch[0]*times
        
        print ques
        
        arr = [None for _ in range(n)]
        i = 0
        cnt = 0
        while cnt < n:
            arr[i] = ques[cnt]
            if i > 0 and arr[i] == arr[i-1]:
                return ""
            i = (i+2)%n
            if i == 0:
                i += 1
            cnt += 1
    
        return "".join(arr)