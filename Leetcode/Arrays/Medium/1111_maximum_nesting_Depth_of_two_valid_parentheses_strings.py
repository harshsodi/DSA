# Runtime: 32 ms, faster than 97.56% of Python online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.
# Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        
        n = len(seq)
        ans = [None for _ in seq]
        
        oa = 0
        ob = 0
        
        for i in range(n):
            if seq[i] == '(': # Opening brac
                if oa > ob:
                    ob += 1
                    ans[i] = 1
                else:
                    oa += 1
                    ans[i] = 0
            else:
                if oa > ob:
                    oa -= 1
                    ans[i] = 0
                else:
                    ob -= 1
                    ans[i] = 1
        
        return ans