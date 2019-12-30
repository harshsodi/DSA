# Runtime: 356 ms, faster than 90.03% of Python online submissions for Task Scheduler.
# Memory Usage: 13.8 MB, less than 26.67% of Python online submissions for Task Scheduler.

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        k = n
        arr = {}
        
        for i in tasks:
            arr[i] = arr.get(i, 0) + 1
        
        arr = sorted(arr.values(), reverse=True)
        n = len(arr)
        
        idle = (arr[0]-1) * k
        h = arr[0] - 1
        for i in range(1, n):
            idle -= min(h, arr[i])
        
        print idle
        
        if idle > 0:
            return idle + len(tasks)
        
        return len(tasks)