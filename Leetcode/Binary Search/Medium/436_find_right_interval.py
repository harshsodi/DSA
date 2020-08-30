# Runtime: 540 ms, faster than 14.51% of Python online submissions for Find Right Interval.
# Memory Usage: 18.4 MB, less than 58.92% of Python online submissions for Find Right Interval.

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        
        # Pair with index
        n = len(intervals)
        pairs = [(intervals[i], i) for i in range(n)]
        pairs = sorted(pairs, key=lambda x: x[0][0])
        
        # print pairs
        
        ans_fin = []
        
        for i_ in range(n):
            
            i = intervals[i_]
            
            ans = None
            target = i[1]
            
            l = 0
            r = n - 1
            
            while l <= r:
                m = (l+r)/2
                
                if pairs[m][0][0] >= target:
                    ans = m
                    r = m - 1
                else:
                    l = m + 1
            
            if ans == None:
                ans_fin.append(-1)
            else:
                ans_fin.append(pairs[ans][1])
        
        return ans_fin