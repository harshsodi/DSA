# Runtime: 60 ms, faster than 77.55% of Python online submissions for Merge Intervals.
# Memory Usage: 14.1 MB, less than 69.19% of Python online submissions for Merge Intervals.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for x in intervals:
            if not merged or merged[-1][1] < x[0]:
                merged.append(x)
            else:
                merged[-1][1] = max(merged[-1][1], x[1])
        
        return merged