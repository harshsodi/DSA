# Runtime: 24 ms, faster than 45.53% of Python online submissions for Video Stitching.
# Memory Usage: 11.7 MB, less than 60.00% of Python online submissions for Video Stitching.

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """

        clips = sorted(clips, key=lambda x: x[0])
        n = len(clips)
        
        last = clips[0]
        
        if last[0] > 0:
            return -1
        
        i = 1
        max_end = -1
        
        while clips[i][0] == clips[i-1][0] and clips[i][1] > clips[i-1][1]:
            if max_end <= clips[i][1]:
                last = clips[i]
                max_end = clips[i][1]
            
            i += 1
        
        ans = 1
        
        while i < n and last[1] < T:
            
            if last[1] < clips[i][0]:
                return -1
            
            max_end = -1
            while i < n and last[1] >= clips[i][0]:
                max_end = max(max_end, clips[i][1])
                i += 1
            
            if max_end > last[1]:
                ans += 1
                last[1] = max_end
        
        if last[1] >= T:
            return ans
        return -1