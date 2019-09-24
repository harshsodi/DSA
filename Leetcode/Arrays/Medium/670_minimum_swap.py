# Runtime: 12 ms, faster than 91.15% of Python online submissions for Maximum Swap.
# Memory Usage: 11.8 MB, less than 60.00% of Python online submissions for Maximum Swap.

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        sn = str(num)
        s = [x for x in str(num)]
        b = [-1 for p in sn]
        l = len(s)
        
        m = l-1
        
        i = l-2
        while i >= 0:
            # print "Comparing: ", s[i], s[m]
            if s[i] < s[m]:
                # print s[i], " < ", s[m]
                b[i] = m
            else:
                if s[i] != s[m]:
                    m = i
            i -= 1
            
        for i in range(l):
            if b[i] != -1:
                tmp = s[i]
                s[i] = s[b[i]]
                s[b[i]] = tmp
                break
        
        return int("".join(s))