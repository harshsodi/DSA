# Runtime: 16 ms, faster than 95.34% of Python online submissions for Generate Parentheses.
# Memory Usage: 12.2 MB, less than 5.88% of Python online submissions for Generate Parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        d = {}
        
        d[1] = set(['()'])
        
        for i in range(2,n+1):
            d[i] = set([])
            
            for l in d[i-1]:                
                d[i].add("(" + l + ")")
            
            for j in range(1, (i/2) + 1):
                k = i - j
                # print j, k
                
                for x in d[j]:
                    for y in d[k]:
                        d[i].add(x+y)
                        d[i].add(y+x)
                        
        return list(d[n])