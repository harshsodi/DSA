# Runtime: 36 ms, faster than 28.89% of Python online submissions for Statistics from a Large Sample.
# Memory Usage: 13 MB, less than 100.00% of Python online submissions for Statistics from a Large Sample.

class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        
        mini = float('inf')
        maxi = 0
        sm = 0.0
        cnt = 0
        
        max_cnt = 0
        mode = None
        
        l = 0
        r = 255
        l_cnt = 0
        r_cnt = 0
        
        while l <= r:
            if l_cnt < r_cnt:
                
                if count[l] > 0:
                    mini = min(mini, l)
                    maxi = max(maxi, l)
                
                if max_cnt < count[l]:
                    max_cnt = count[l]
                    mode = l
                
                sm += count[l]*l
                cnt += count[l]
                
                l_cnt += count[l]
                l += 1
            else:
                if count[r] > 0:
                    mini = min(mini, r) 
                    maxi = max(maxi, r)
                
                if max_cnt < count[r]:
                    max_cnt = count[r]
                    mode = r
                
                sm += count[r]*r
                cnt += count[r]
                
                r_cnt += count[r]
                r -= 1
                
        mean = sm/cnt
        median = None
        
        if l_cnt == r_cnt:
            median = (l + r) / 2.0
        elif l_cnt > r_cnt:
            median = l - 1
        else:
            median = r + 1
        
        return [mini, maxi, mean, median, mode]
        