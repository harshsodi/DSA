# Runtime: 56 ms, faster than 75.42% of Python online submissions for Insert Interval.
# Memory Usage: 15.2 MB, less than 71.85% of Python online submissions for Insert Interval.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        if not len(intervals):
            return [newInterval]
        
        ilen = len(intervals) - 1
        
        flag = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                flag = 1
                break
            
        # Insert at ith index
        if flag:
            temp = intervals[i]
            intervals.append(intervals[ilen])
            ilen += 1

            while ilen > i:
                intervals[ilen] = intervals[ilen-1]
                ilen -= 1

            intervals[i] = newInterval
        else:
            intervals.append(newInterval)
        
        merged = []
        
        for x in intervals:
            if not merged or merged[-1][1] < x[0]:
                merged.append(x)
            else:
                merged[-1][1] = max(merged[-1][1], x[1])
        
        return merged